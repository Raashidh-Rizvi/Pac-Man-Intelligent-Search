#!/usr/bin/env python3
"""
Exhaustive admissibility and consistency checker for the Q6/Q7 heuristics.

For a given search problem this script:

  1. enumerates every state reachable from the start state;
  2. computes the true cost-to-go h* for each one, by reversing the state graph
     and running a breadth-first sweep outward from the goal states;
  3. asserts h(s) <= h*(s) for every state            (admissibility);
  4. asserts h(s) <= c(s, s') + h(s') for every edge   (consistency);
  5. asserts h(s) == 0 at every goal state and h(s) >= 0 everywhere.

Any violation is printed with the offending state, so a failure is actionable
rather than just a red cross.

Usage:
    python tools/verify_heuristics.py
"""

import os
import sys
from collections import deque

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import layout                                  # noqa: E402
import searchAgents                            # noqa: E402
from pacman import GameState                   # noqa: E402


def buildProblem(problemClass, layoutName):
    lay = layout.getLayout(layoutName)
    if lay is None:
        raise SystemExit('Layout not found: %s' % layoutName)
    state = GameState()
    state.initialize(lay, 0)
    return problemClass(state)


def analyse(problem, heuristic, label, keyOf=lambda state: state):
    """Enumerate the state space and check the heuristic over all of it."""
    start = problem.getStartState()

    # Forward sweep: collect every reachable state and the edges between them.
    edges = {}
    seen = {keyOf(start): start}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        key = keyOf(state)
        if problem.isGoalState(state):
            edges[key] = []
            continue
        successors = []
        for nextState, _action, cost in problem.getSuccessors(state):
            nextKey = keyOf(nextState)
            successors.append((nextKey, cost))
            if nextKey not in seen:
                seen[nextKey] = nextState
                queue.append(nextState)
        edges[key] = successors

    # Reverse sweep from the goal states gives the exact cost-to-go h*.
    reverse = {key: [] for key in edges}
    for key, successors in edges.items():
        for nextKey, _cost in successors:
            reverse[nextKey].append(key)
    costToGo = {}
    queue = deque()
    for key, state in seen.items():
        if problem.isGoalState(state):
            costToGo[key] = 0
            queue.append(key)
    while queue:
        key = queue.popleft()
        for previousKey in reverse[key]:
            if previousKey not in costToGo:
                costToGo[previousKey] = costToGo[key] + 1
                queue.append(previousKey)

    values = {}
    admissibility, consistency, goalValues, negatives = [], [], [], []
    for key, state in seen.items():
        value = heuristic(state, problem)
        values[key] = value
        if value < 0:
            negatives.append((key, value))
        if problem.isGoalState(state) and value != 0:
            goalValues.append((key, value))
        if key in costToGo and value > costToGo[key]:
            admissibility.append((key, value, costToGo[key]))
    for key, successors in edges.items():
        for nextKey, cost in successors:
            if values[key] > cost + values[nextKey]:
                consistency.append((key, nextKey, values[key], cost, values[nextKey]))

    startKey = keyOf(start)
    print('\n===== %s =====' % label)
    print('states reachable : %d' % len(seen))
    print('h(start)         : %s   (true optimal cost %s)'
          % (values[startKey], costToGo.get(startKey)))

    def report(name, violations, formatter):
        ok = not violations
        print('%-17s: %s' % (name, 'PASS' if ok else 'FAIL (%d violations)' % len(violations)))
        for violation in violations[:5]:
            print('    %s' % formatter(violation))
        return ok

    allOk = True
    allOk &= report('non-negative', negatives, lambda v: 'state=%s h=%s' % v)
    allOk &= report('h(goal) == 0', goalValues, lambda v: 'state=%s h=%s' % v)
    allOk &= report('admissible', admissibility,
                    lambda v: 'state=%s  h=%s > h*=%s' % v)
    allOk &= report('consistent', consistency,
                    lambda v: '%s -> %s   h(s)=%s > c=%s + h(s\')=%s' % v)
    return allOk


def foodKey(state):
    """Food grids are unhashable, so key on the sorted list of remaining dots."""
    return (state[0], tuple(sorted(state[1].asList())))


def main():
    results = []
    for layoutName in ('tinyCorners', 'mediumCorners'):
        results.append(analyse(
            buildProblem(searchAgents.CornersProblem, layoutName),
            searchAgents.cornersHeuristic,
            'Q6 cornersHeuristic on %s' % layoutName))

    for layoutName in ('tinyMaze', 'tinyCorners'):
        results.append(analyse(
            buildProblem(searchAgents.FoodSearchProblem, layoutName),
            searchAgents.foodHeuristic,
            'Q7 foodHeuristic on %s' % layoutName,
            foodKey))

    print('\n' + '=' * 46)
    if all(results):
        print('ALL CHECKS PASSED')
        return 0
    print('CHECKS FAILED')
    return 1


if __name__ == '__main__':
    sys.exit(main())
