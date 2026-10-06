"""Member 3 regressions; independent of the custom and Berkeley graders.

Run from the repository root: python -B -m unittest discover -s tests -v
"""
import contextlib
import io
import itertools
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import layout
from pacman import GameState
import search
import searchAgents


def make_game():
    # Each corner contains food; Pac-Man starts in the center.
    game = GameState()
    game.initialize(layout.Layout([
        "%%%%%", "%. .%", "% P %", "%. .%", "%%%%%"
    ]), 0)
    return game


class SearchAgentTests(unittest.TestCase):
    def test_selected_manhattan_is_called_by_astar(self):
        original = searchAgents.manhattanHeuristic
        for name in ("astar", "aStarSearch"):
            with self.subTest(function=name):
                with patch.object(searchAgents, "manhattanHeuristic", wraps=original) as heuristic:
                    agent = searchAgents.SearchAgent(fn=name, heuristic="manhattanHeuristic")
                    with contextlib.redirect_stdout(io.StringIO()):
                        agent.registerInitialState(make_game())
                    self.assertGreater(heuristic.call_count, 0)
                    state, problem = heuristic.call_args_list[0].args
                    self.assertEqual(state, problem.getStartState())
                    self.assertEqual(problem.getCostOfActions(agent.actions), 2)

    def test_nonheuristic_functions_still_work(self):
        for name in ("bfs", "dfs", "ucs"):
            with self.subTest(function=name):
                with patch.object(searchAgents, "manhattanHeuristic",
                                  side_effect=AssertionError("Heuristic must not be used")):
                    agent = searchAgents.SearchAgent(fn=name, heuristic="manhattanHeuristic")
                    with contextlib.redirect_stdout(io.StringIO()):
                        agent.registerInitialState(make_game())
                    problem = searchAgents.PositionSearchProblem(make_game())
                    state = problem.getStartState()
                    for action in agent.actions:
                        state = next(t for t, a, _ in problem.getSuccessors(state) if a == action)
                    self.assertTrue(problem.isGoalState(state))

    def test_default_null_heuristic_matches_ucs(self):
        agent = searchAgents.SearchAgent(fn="astar")
        with contextlib.redirect_stdout(io.StringIO()):
            agent.registerInitialState(make_game())
        self.assertEqual(agent.actions, search.ucs(searchAgents.PositionSearchProblem(make_game())))


class CornersContractTests(unittest.TestCase):
    def setUp(self):
        self.problem = searchAgents.CornersProblem(make_game())

    def test_start_corner_flags_and_hashability(self):
        self.assertEqual(self.problem.corners, ((1, 1), (1, 3), (3, 1), (3, 3)))
        for position in self.problem.corners + ((2, 2),):
            self.problem.startingPosition = position
            state = self.problem.getStartState()
            expected = (position, tuple(position == corner for corner in self.problem.corners))
            self.assertEqual(state, expected)
            self.assertIn(state, {state})
            self.assertTrue(all(type(flag) is bool for flag in state[1]))

    def test_goal_requires_all_four_flags(self):
        for flags in itertools.product((False, True), repeat=4):
            self.assertEqual(self.problem.isGoalState(((2, 2), flags)), sum(flags) == 4)

    def test_successors_walls_aliasing_revisits_and_expansion_count(self):
        state = ((1, 2), (False, False, False, False))
        successors = self.problem.getSuccessors(state)
        self.assertEqual(self.problem._expanded, 1)
        self.assertEqual([a for _, a, _ in successors], ["North", "South", "East"])
        by_action = {action: successor for successor, action, _ in successors}
        self.assertEqual(by_action["North"], ((1, 3), (False, True, False, False)))
        self.assertEqual(by_action["South"], ((1, 1), (True, False, False, False)))
        self.assertEqual(by_action["East"], ((2, 2), state[1]))
        self.assertEqual(state, ((1, 2), (False, False, False, False)))
        for successor, _, cost in successors:
            self.assertEqual(cost, 1)
            self.assertIn(successor, {successor})
        down = next(t for t, a, _ in self.problem.getSuccessors(by_action["North"]) if a == "South")
        revisit = next(t for t, a, _ in self.problem.getSuccessors(down) if a == "North")
        self.assertEqual(revisit, by_action["North"])
        self.assertEqual(self.problem._expanded, 3)

    def test_action_costs(self):
        self.assertEqual(self.problem.getCostOfActions(None), 999999)
        self.assertEqual(self.problem.getCostOfActions([]), 0)
        self.assertEqual(self.problem.getCostOfActions(["West", "South"]), 2)
        self.assertEqual(self.problem.getCostOfActions(["West", "West"]), 999999)
        self.assertEqual(self.problem._expanded, 0)


if __name__ == "__main__":
    unittest.main()
