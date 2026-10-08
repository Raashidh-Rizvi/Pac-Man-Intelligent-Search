# searchAgents.py
# ---------------
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
This file contains all of the agents that can be selected to control Pacman.  To
select an agent, use the '-p' option when running pacman.py.  Arguments can be
passed to the agent using the '-a' option.  For example, to load a SearchAgent
that uses depth first search to find a path to the Coord(4,5), run the following
command:

> python pacman.py -p SearchAgent -a fn=depthFirstSearch,prob=PositionSearchProblem,target=(4,5)
"""

from game import Directions
from game import Agent
from game import Actions
import util
import time
import search

class GoWestAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP

class SearchAgent(Agent):
    """
    This general search agent finds a path using a supplied search
    algorithm for a supplied search problem, then returns actions to follow that
    path.
    """

    def __init__(self, fn='depthFirstSearch', prob='PositionSearchProblem', heuristic='nullHeuristic'):
        # Get the search function from the name and module
        if fn not in dir(search):
            raise AttributeError(fn + ' is not a search function in search.py.')
        self.searchFunction = getattr(search, fn)

        # Get the SearchProblem the agent should use
        if prob not in globals():
            raise AttributeError(prob + ' is not a SearchProblem type in searchAgents.py.')
        self.problemType = globals()[prob]

        # Get the heuristic function
        if heuristic in globals():
            self.heuristicFunction = globals()[heuristic]
        elif heuristic in dir(search):
            self.heuristicFunction = getattr(search, heuristic)
        else:
            raise AttributeError(heuristic + ' is not a heuristic function in searchAgents.py or search.py.')

        # Bind the heuristic for A*, as in the official SearchAgent.
        searchFunction = self.searchFunction
        if 'heuristic' in searchFunction.__code__.co_varnames:
            self.searchFunction = lambda problem: searchFunction(problem, heuristic=self.heuristicFunction)

    def registerInitialState(self, state):
        """
        This is the first time that the agent sees the layout of the game
        board. Here, we choose a path to the goal. In this phase, the agent
        should compute the path to the goal and store it in a local variable.
        """
        if self.searchFunction == None: raise Exception("No search function provided for SearchAgent")
        starttime = time.time()
        problem = self.problemType(state) # Makes the problem
        self.actions  = self.searchFunction(problem) # Finds a path
        totalCost = problem.getCostOfActions(self.actions)
        print('Path found with total cost of %d in %.1f seconds' % (totalCost, time.time() - starttime))
        if '_expanded' in dir(problem): print('Search nodes expanded: %d' % problem._expanded)

    def getAction(self, state):
        """
        Returns the next action in the path given during the registerInitialState phase.
        """
        if 'actionIndex' not in dir(self): self.actionIndex = 0
        i = self.actionIndex
        self.actionIndex += 1
        if i < len(self.actions):
            return self.actions[i]
        else:
            return Directions.STOP

class PositionSearchProblem(search.SearchProblem):
    """
    A search problem defines the state space, start state, goal test, successor
    function and cost function.  This search problem can be used to find paths
    to a particular point on the pacman board.
    """

    def __init__(self, gameState, costFn = lambda x: 1, goal=(1,1), start=None, warn=True, visualize=True):
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition()
        if start != None: self.startState = start
        self.goal = goal
        if gameState.getNumFood() > 0:
            foodList = gameState.getFood().asList()
            if goal == (1, 1) and (goal not in foodList or self.startState == goal):
                self.goal = foodList[0]
        self.costFn = costFn
        self.visualize = visualize

        # For display purposes
        self._visited, self._visitedlist, self._expanded = {}, [], 0

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        isGoal = state == self.goal

        # For display purposes only
        if isGoal and self.visualize:
            self._visitedlist.append(state)
            import __main__
            if '_display' in dir(__main__):
                if 'drawExpandedCells' in dir(__main__._display):
                    __main__._display.drawExpandedCells(self._visitedlist)
        return isGoal

    def getSuccessors(self, state):
        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x,y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                cost = self.costFn(nextState)
                successors.append( ( nextState, action, cost) )

        # Bookkeeping for display purposes
        self._expanded += 1
        if state not in self._visited:
            self._visited[state] = True
            self._visitedlist.append(state)

        return successors

    def getCostOfActions(self, actions):
        if actions == None: return 999999
        x,y= self.getStartState()
        cost = 0
        for action in actions:
            # Check if action is valid
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
            cost += self.costFn((x,y))
        return cost

def manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def euclideanHeuristic(position, problem, info={}):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5


class CornersProblem(search.SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.
    """

    def __init__(self, startingGameState):
        """
        Stores the walls, corners, and start state.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = ((1,1), (1,top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print('Warning: no food in corner ' + str(corner))
        self._expanded = 0

    def getStartState(self):
        """
        Returns the start state.
        """
        startVisited = tuple(self.startingPosition == corner for corner in self.corners)
        return (self.startingPosition, startVisited)

    def isGoalState(self, state):
        """
        Returns whether this search state is a goal state of the problem.
        """
        return all(state[1])

    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.
        """
        successors = []
        x, y = state[0]
        visited = list(state[1])

        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextPos = (nextx, nexty)
                nextVisited = list(visited)
                if nextPos in self.corners:
                    idx = self.corners.index(nextPos)
                    nextVisited[idx] = True
                successors.append(((nextPos, tuple(nextVisited)), action, 1))

        self._expanded += 1
        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.
        """
        if actions == None: return 999999
        x,y= self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)


def cornerMazeDistances(problem):
    """
    Computes and caches all-pairs shortest maze distances from every corner to
    every reachable tile in the maze using BFS. Returns a dict mapping:
    corner -> { (x, y): maze_distance }
    """
    if hasattr(problem, '_cornerMazeDistances'):
        return problem._cornerMazeDistances

    walls = problem.walls
    distanceMaps = {}

    for corner in problem.corners:
        dist = {}
        queue = util.Queue()
        queue.push((corner, 0))
        dist[corner] = 0

        while not queue.isEmpty():
            curr, d = queue.pop()
            x, y = curr
            for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
                dx, dy = Actions.directionToVector(action)
                nextx, nexty = int(x + dx), int(y + dy)
                nextPos = (nextx, nexty)
                if not walls[nextx][nexty] and nextPos not in dist:
                    dist[nextPos] = d + 1
                    queue.push((nextPos, d + 1))

        distanceMaps[corner] = dist

    problem._cornerMazeDistances = distanceMaps
    return distanceMaps


def cornersHeuristic(state, problem):
    """
    Admissible and consistent tour heuristic for the CornersProblem.

    Computes the exact length of the shortest path starting at `position` and
    visiting all remaining unvisited corners in ANY order, where distances
    between points are true maze distances (BFS shortest paths).

    Admissible: any valid solution must physically visit all unvisited corners
    in some order, and each of its legs is at least the maze distance between that
    leg's endpoints.  So the real cost is at least the cost of that ordering, which
    is at least the minimum over all orderings.

    Consistent: the value is the exact goal distance of a relaxed problem in which
    travelling from a square to a corner costs the maze distance between them.  For
    a step that eats no corner, the triangle inequality gives
    d(p, c) <= 1 + d(p', c), so h(s) <= 1 + h(s').  For a step onto a new corner c,
    visiting c first is one candidate ordering, so h(s) <= 1 + h(s') as well.

    Zero at every goal state, since no corners remain to be visited.
    """
    from itertools import permutations

    position, visited = state
    corners = problem.corners
    outstanding = tuple(corners[i] for i in range(len(corners)) if not visited[i])
    if not outstanding:
        return 0

    if not hasattr(problem, '_cornersHeuristicCache'):
        problem._cornersHeuristicCache = {}
    cache = problem._cornersHeuristicCache
    cacheKey = (position, outstanding)
    if cacheKey in cache:
        return cache[cacheKey]

    distanceMaps = cornerMazeDistances(problem)
    best = None
    for order in permutations(outstanding):
        # Maze distance is symmetric, so the map keyed on a corner also gives the
        # distance from an arbitrary square to that corner.
        total = distanceMaps[order[0]][position]
        for current, nextCorner in zip(order, order[1:]):
            total += distanceMaps[current][nextCorner]
        if best is None or total < best:
            best = total

    cache[cacheKey] = best
    return best


class AStarCornersAgent(SearchAgent):
    "A SearchAgent for the CornersProblem using A* and cornersHeuristic."
    def __init__(self):
        self.searchFunction = lambda prob: search.aStarSearch(prob, cornersHeuristic)
        self.problemType = CornersProblem


class FoodSearchProblem:
    """
    A search problem associated with finding the paths that collect all of the
    food (dots) in a Pacman game.
    """
    def __init__(self, startingGameState):
        self.start = (startingGameState.getPacmanPosition(), startingGameState.getFood())
        self.walls = startingGameState.getWalls()
        self.startingGameState = startingGameState
        self._expanded = 0
        self.heuristicInfo = {}

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state[1].count() == 0

    def getSuccessors(self, state):
        "Returns successor states, the actions they require, and a cost of 1."
        successors = []
        self._expanded += 1
        for direction in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x,y = state[0]
            dx, dy = Actions.directionToVector(direction)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextFood = state[1].copy()
                nextFood[nextx][nexty] = False
                successors.append( ( ((nextx, nexty), nextFood), direction, 1) )
        return successors

    def getCostOfActions(self, actions):
        """Returns the cost of a particular sequence of actions."""
        x,y= self.getStartState()[0]
        cost = 0
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
            cost += 1
        return cost


def foodHeuristic(state, problem):
    """
    An admissible and consistent heuristic for FoodSearchProblem using
    the distance to the nearest food plus the Minimum Spanning Tree (MST)
    cost of the remaining food items based on true maze distances.
    """
    position, foodGrid = state
    foodList = foodGrid.asList()
    if not foodList:
        return 0

    # Cache pairwise maze distances in problem.heuristicInfo
    if 'dist_cache' not in problem.heuristicInfo:
        problem.heuristicInfo['dist_cache'] = {}
    
    cache = problem.heuristicInfo['dist_cache']

    def getMazeDistance(p1, p2):
        if p1 == p2:
            return 0
        key = (p1, p2) if p1 < p2 else (p2, p1)
        if key not in cache:
            walls = problem.walls
            queue = util.Queue()
            queue.push((p1, 0))
            visited = {p1}
            dist = 0
            while not queue.isEmpty():
                curr, d = queue.pop()
                if curr == p2:
                    dist = d
                    break
                cx, cy = curr
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if not walls[nx][ny] and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.push(((nx, ny), d + 1))
            cache[key] = dist
        return cache[key]

    # Distance from Pac-Man to nearest food
    closest_dist = min(getMazeDistance(position, food) for food in foodList)

    if len(foodList) == 1:
        return closest_dist

    # Prim's algorithm to calculate MST cost for remaining food items
    mst_cost = 0
    unvisited = set(foodList)
    start_node = unvisited.pop()
    min_dist = {node: getMazeDistance(start_node, node) for node in unvisited}

    while unvisited:
        next_node = min(unvisited, key=lambda n: min_dist[n])
        mst_cost += min_dist[next_node]
        unvisited.remove(next_node)

        for node in unvisited:
            d = getMazeDistance(next_node, node)
            if d < min_dist[node]:
                min_dist[node] = d

    return closest_dist + mst_cost


class ClosestDotSearchAgent(SearchAgent):
    "Search for all food using a sequence of searches"
    def registerInitialState(self, state):
        self.actions = []
        currentState = state
        while(currentState.getFood().count() > 0):
            nextPathSegment = self.findPathToClosestDot(currentState)
            self.actions += nextPathSegment
            for action in nextPathSegment:
                legal = currentState.getLegalActions()
                if action not in legal:
                    raise Exception('findPathToClosestDot returned an illegal move: %s!\n%s' % (action, currentState))
                currentState = currentState.generatePacmanSuccessor(action)
        self.actionIndex = 0
        print('Path found with total cost of %d.' % len(self.actions))

    def findPathToClosestDot(self, gameState):
        """
        Returns a path (a list of actions) to the closest dot, starting from
        gameState.
        """
        problem = AnyFoodSearchProblem(gameState)
        return search.bfs(problem)

class AnyFoodSearchProblem(PositionSearchProblem):
    """
    A search problem for finding a path to any food.
    """
    def __init__(self, gameState):
        "Stores information from the gameState.  You don't need to change this."
        self.food = gameState.getFood()
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition()
        self.costFn = lambda x: 1
        self._visited, self._visitedlist, self._expanded = {}, [], 0

    def isGoalState(self, state):
        x,y = state
        return self.food[x][y]
