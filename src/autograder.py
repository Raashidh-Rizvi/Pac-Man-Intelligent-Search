# autograder.py
# -------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import sys
import os
import optparse
import layout
from game import Actions
from pacman import GameState
import search
import searchAgents

def readCommand(argv):
    parser = optparse.OptionParser(description='Run public autograder tests for Pac-Man Search.')
    parser.add_option('-q', '--question', dest='question', default=None,
                      help='Run tests for a specific question (e.g. q1, q2, q3, q4, q5, q6, q7)')
    parser.add_option('-t', '--test', dest='test', default=None,
                      help='Run a specific test case file')
    options, args = parser.parse_args(argv)
    return options

def testPositionSearch(layoutName, searchFunc, heuristic=None):
    lay = layout.getLayout(layoutName)
    if not lay:
        return False, f"Layout {layoutName} not found", 0, 0
    state = GameState()
    state.initialize(lay, 0)
    prob = searchAgents.PositionSearchProblem(state, warn=False)
    
    try:
        if heuristic:
            actions = searchFunc(prob, heuristic)
        else:
            actions = searchFunc(prob)
    except Exception as e:
        return False, f"Execution raised Exception: {e}", 0, 0

    if not isinstance(actions, list):
        return False, f"Returned actions is not a list (got {type(actions)})", 0, 0

    cost = prob.getCostOfActions(actions)
    curr = prob.getStartState()
    for act in actions:
        dx, dy = Actions.directionToVector(act)
        next_pos = (int(curr[0] + dx), int(curr[1] + dy))
        if state.getWalls()[next_pos[0]][next_pos[1]]:
            return False, f"Illegal move {act} into wall at {next_pos}", cost, prob._expanded
        curr = next_pos

    if curr != prob.goal:
        return False, f"Path ended at {curr} instead of goal {prob.goal}", cost, prob._expanded

    return True, "Valid path to goal", cost, prob._expanded

def testCornersSearch(layoutName, searchFunc, heuristic=None):
    lay = layout.getLayout(layoutName)
    if not lay:
        return False, f"Layout {layoutName} not found", 0, 0
    state = GameState()
    state.initialize(lay, 0)
    prob = searchAgents.CornersProblem(state)
    
    try:
        if heuristic:
            actions = searchFunc(prob, heuristic)
        else:
            actions = searchFunc(prob)
    except Exception as e:
        return False, f"Execution raised Exception: {e}", 0, 0

    if not isinstance(actions, list):
        return False, f"Returned actions is not a list (got {type(actions)})", 0, 0

    cost = prob.getCostOfActions(actions)
    
    # Verify path visits all corners
    currState = prob.getStartState()
    visitedCorners = set()
    if currState[0] in prob.corners:
        visitedCorners.add(currState[0])

    currPos = currState[0]
    for act in actions:
        dx, dy = Actions.directionToVector(act)
        next_pos = (int(currPos[0] + dx), int(currPos[1] + dy))
        if state.getWalls()[next_pos[0]][next_pos[1]]:
            return False, f"Illegal move {act} into wall at {next_pos}", cost, prob._expanded
        currPos = next_pos
        if currPos in prob.corners:
            visitedCorners.add(currPos)

    if len(visitedCorners) < 4:
        return False, f"Path visited only {len(visitedCorners)}/4 corners", cost, prob._expanded

    return True, "Visited all 4 corners", cost, prob._expanded

def testFoodSearch(layoutName, searchFunc, heuristic=None):
    lay = layout.getLayout(layoutName)
    if not lay:
        return False, f"Layout {layoutName} not found", 0, 0
    state = GameState()
    state.initialize(lay, 0)
    prob = searchAgents.FoodSearchProblem(state)

    try:
        if heuristic:
            actions = searchFunc(prob, heuristic)
        else:
            actions = searchFunc(prob)
    except Exception as e:
        return False, f"Execution raised Exception: {e}", 0, 0

    if not isinstance(actions, list):
        return False, f"Returned actions is not a list (got {type(actions)})", 0, 0

    cost = prob.getCostOfActions(actions)
    return True, "Collected food successfully", cost, prob._expanded


QUESTION_SCORES = {}

def runQuestion(question_name):
    q_key = question_name.lower()
    print(f"\n=== Running Autograder for Question: {q_key.upper()} ===")

    score = 0
    max_score = 0

    if q_key == 'q1':
        title = "Depth First Search (DFS)"
        max_score = 3
        ok1, msg1, c1, e1 = testPositionSearch('tinyMaze', search.dfs)
        ok2, msg2, c2, e2 = testPositionSearch('mediumMaze', search.dfs)
        print(f"  Test 1 (tinyMaze): {'PASS' if ok1 else 'FAIL'} - {msg1} (cost: {c1}, expanded: {e1})")
        print(f"  Test 2 (mediumMaze): {'PASS' if ok2 else 'FAIL'} - {msg2} (cost: {c2}, expanded: {e2})")
        if ok1 and ok2:
            score = 3

    elif q_key == 'q2':
        title = "Breadth First Search (BFS)"
        max_score = 3
        ok1, msg1, c1, e1 = testPositionSearch('tinyMaze', search.bfs)
        ok2, msg2, c2, e2 = testPositionSearch('mediumMaze', search.bfs)
        print(f"  Test 1 (tinyMaze): {'PASS' if ok1 else 'FAIL'} - {msg1} (cost: {c1}, expanded: {e1})")
        print(f"  Test 2 (mediumMaze): {'PASS' if ok2 else 'FAIL'} - {msg2} (cost: {c2}, expanded: {e2})")
        if ok1 and ok2 and c1 == 6 and c2 == 20:
            score = 3

    elif q_key == 'q3':
        title = "Uniform Cost Search (UCS)"
        max_score = 3
        ok1, msg1, c1, e1 = testPositionSearch('mediumMaze', search.ucs)
        print(f"  Test 1 (mediumMaze): {'PASS' if ok1 else 'FAIL'} - {msg1} (cost: {c1}, expanded: {e1})")
        if ok1 and c1 == 20:
            score = 3

    elif q_key == 'q4':
        title = "A* Search"
        max_score = 3
        ok1, msg1, c1, e1 = testPositionSearch('mediumMaze', search.astar, searchAgents.manhattanHeuristic)
        print(f"  Test 1 (mediumMaze + Manhattan): {'PASS' if ok1 else 'FAIL'} - {msg1} (cost: {c1}, expanded: {e1})")
        if ok1 and c1 == 20 and e1 <= 100:
            score = 3

    elif q_key == 'q5':
        title = "Corners Problem State Space"
        max_score = 3
        ok1, msg1, c1, e1 = testCornersSearch('tinyCorners', search.bfs)
        ok2, msg2, c2, e2 = testCornersSearch('mediumCorners', search.bfs)
        print(f"  Test 1 (tinyCorners BFS): {'PASS' if ok1 else 'FAIL'} - {msg1} (cost: {c1}, expanded: {e1})")
        print(f"  Test 2 (mediumCorners BFS): {'PASS' if ok2 else 'FAIL'} - {msg2} (cost: {c2}, expanded: {e2})")
        if ok1 and ok2:
            score = 3

    elif q_key == 'q6':
        title = "Corners Heuristic"
        max_score = 3
        ok1, msg1, c1, e1 = testCornersSearch('mediumCorners', search.astar, searchAgents.cornersHeuristic)
        print(f"  Test 1 (mediumCorners A* + Heuristic): {'PASS' if ok1 else 'FAIL'} - {msg1} (cost: {c1}, expanded: {e1})")
        if ok1 and c1 == 42 and e1 <= 600:
            score = 3

    elif q_key == 'q7':
        title = "Food Heuristic"
        max_score = 4
        ok1, msg1, c1, e1 = testFoodSearch('mediumMaze', search.astar, searchAgents.foodHeuristic)
        print(f"  Test 1 (mediumMaze Food A*): {'PASS' if ok1 else 'FAIL'} - {msg1} (cost: {c1}, expanded: {e1})")
        if ok1:
            score = 4

    else:
        print(f"Unknown question: {question_name}. Valid options: q1, q2, q3, q4, q5, q6, q7")
        return False

    QUESTION_SCORES[q_key] = (score, max_score, title)
    print(f"  ---> Question {q_key.upper()} Score: {score}/{max_score} points")
    return score == max_score

def runAll():
    print("==================================================")
    print("  PAC-MAN INTELLIGENT SEARCH AUTOGRADER SUITE    ")
    print("==================================================")
    total_pts = 0
    total_max = 0
    for q in ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']:
        runQuestion(q)

    print("\n" + "="*50)
    print("      FINAL GRADED SCORE SUMMARY")
    print("="*50)
    for q_key in ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']:
        if q_key in QUESTION_SCORES:
            s, m, t = QUESTION_SCORES[q_key]
            status = "PASSED" if s == m else "FAILED"
            print(f"  Question {q_key.upper()} ({t}): {s}/{m} points [{status}]")
            total_pts += s
            total_max += m

    print("-" * 50)
    print(f"  TOTAL AUTOGRADER SCORE: {total_pts}/{total_max} points ({(total_pts/total_max)*100:.1f}%)")
    print("="*50 + "\n")

if __name__ == '__main__':
    options = readCommand(sys.argv[1:])
    if options.question:
        runQuestion(options.question)
    else:
        runAll()
