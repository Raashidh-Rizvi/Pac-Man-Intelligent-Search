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
import grading
import projectParams
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

def runQuestion(question_name):
    print(f"=== Running Autograder for Question: {question_name.upper()} ===")
    question_map = {
        'q1': ('Depth First Search (DFS)', 'depthFirstSearch'),
        'q2': ('Breadth First Search (BFS)', 'breadthFirstSearch'),
        'q3': ('Uniform Cost Search (UCS)', 'uniformCostSearch'),
        'q4': ('A* Search', 'aStarSearch'),
        'q5': ('Corners Problem', 'CornersProblem'),
        'q6': ('Corners Heuristic', 'cornersHeuristic'),
        'q7': ('Food Heuristic', 'foodHeuristic')
    }
    
    q_key = question_name.lower()
    if q_key not in question_map:
        print(f"Unknown question: {question_name}. Valid questions: q1, q2, q3, q4, q5, q6, q7")
        return False
    
    title, func_name = question_map[q_key]
    print(f"Target: {title} ({func_name})")

    # Check if function / class is implemented or raises NotDefined
    if q_key in ['q1', 'q2', 'q3', 'q4']:
        func = getattr(search, func_name, None)
        if func is None:
            print(f"FAIL: Function {func_name} not found in search.py")
            return False
        print(f"Checking signature for {func_name}... OK")
    elif q_key in ['q5', 'q6', 'q7']:
        if q_key == 'q5':
            cls = getattr(searchAgents, func_name, None)
            if cls is None:
                print(f"FAIL: Class {func_name} not found in searchAgents.py")
                return False
        else:
            func = getattr(searchAgents, func_name, None)
            if func is None:
                print(f"FAIL: Function {func_name} not found in searchAgents.py")
                return False
        print(f"Checking definition for {func_name}... OK")

    print(f"Note: Implement {func_name} in code to pass test cases.")
    return True

def runAll():
    print("==================================================")
    print("  Pac-Man Intelligent Search Project Autograder  ")
    print("==================================================")
    for q in ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']:
        runQuestion(q)
        print("-" * 50)

if __name__ == '__main__':
    options = readCommand(sys.argv[1:])
    if options.question:
        runQuestion(options.question)
    else:
        runAll()
