# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology, an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
          actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """
    frontier = util.Stack()
    startState = problem.getStartState()
    frontier.push((startState, []))
    visited = set()

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    frontier.push((successor, actions + [action]))

    return []

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [Question 2 Implementation by Member 2: Atheek Fareez]
    """
    # =========================================================================
    # STEP 1: Initialize the Frontier (Fringe) Data Structure
    # -------------------------------------------------------------------------
    # BFS requires a FIFO (First-In, First-Out) Queue so that nodes at the
    # shallowest depth are always expanded first before deeper levels.
    # We use util.Queue provided by the project framework.
    # =========================================================================
    frontier = util.Queue()

    # =========================================================================
    # STEP 2: Get the Initial Start State & Push to Frontier
    # -------------------------------------------------------------------------
    # Each entry in the frontier is a tuple: (current_state, path_of_actions)
    # At start, actions list is empty [] because Pac-Man has not moved yet.
    # =========================================================================
    startState = problem.getStartState()
    frontier.push((startState, []))

    # =========================================================================
    # STEP 3: Initialize the Visited (Expanded) Set for Graph Search
    # -------------------------------------------------------------------------
    # Pac-Man mazes contain cycles (loops). We must remember expanded states
    # so we never expand the same state twice, avoiding infinite loops.
    # =========================================================================
    visited = set()

    # =========================================================================
    # STEP 4: Main Search Loop
    # -------------------------------------------------------------------------
    # Continue expanding nodes until either:
    # 1. The goal state is reached (success), or
    # 2. The frontier becomes empty (no solution exists).
    # =========================================================================
    while not frontier.isEmpty():
        # Pop the oldest unexpanded node from the front of the FIFO Queue
        state, actions = frontier.pop()

        # STEP 4.1: Goal Test
        # Check if the current popped state satisfies the problem goal
        if problem.isGoalState(state):
            return actions

        # STEP 4.2: Graph Search Check
        # Only expand this state if it has NOT been expanded previously
        if state not in visited:
            # Mark this state as expanded
            visited.add(state)

            # STEP 4.3: Expand Successors (Neighbors)
            # problem.getSuccessors(state) returns a list of:
            # (next_state, action_taken, step_cost)
            for successor, action, stepCost in problem.getSuccessors(state):
                # Only enqueue successors that are not already visited
                if successor not in visited:
                    # Accumulate the action path and push to the FIFO queue
                    newActions = actions + [action]
                    frontier.push((successor, newActions))

    # Return empty list if no path to the goal is found
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    startState = problem.getStartState()
    frontier.push((startState, [], 0), 0)
    visited = {}

    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited or cost < visited[state]:
            visited[state] = cost
            for successor, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost
                if successor not in visited or newCost < visited[successor]:
                    frontier.update((successor, actions + [action], newCost), newCost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()
    startState = problem.getStartState()
    startHeuristic = heuristic(startState, problem)
    frontier.push((startState, [], 0), startHeuristic)
    visited = {}

    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited or cost < visited[state]:
            visited[state] = cost
            for successor, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost
                if successor not in visited or newCost < visited[successor]:
                    priority = newCost + heuristic(successor, problem)
                    frontier.update((successor, actions + [action], newCost), priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
