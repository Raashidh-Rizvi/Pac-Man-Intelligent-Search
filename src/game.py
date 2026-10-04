# game.py
# -------
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


from util import *
import time, os, traceback

class Directions:
    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'
    STOP = 'Stop'

    LEFT = {NORTH: WEST,
            SOUTH: EAST,
            EAST: NORTH,
            WEST: SOUTH,
            STOP: STOP}

    RIGHT = dict([(y, x) for x, y in list(LEFT.items())])

    REVERSE = {NORTH: SOUTH,
               SOUTH: NORTH,
               EAST: WEST,
               WEST: EAST,
               STOP: STOP}

class Configuration:
    """
    A Configuration holds the (x,y) coordinate of a character, along with its
    traveling direction.
    """

    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction

    def getPosition(self):
        return self.pos

    def getDirection(self):
        return self.direction

    def isInteger(self):
        x, y = self.pos
        return x == int(x) and y == int(y)

    def __eq__(self, other):
        if other == None: return False
        return (self.pos == other.pos and self.direction == other.direction)

    def __hash__(self):
        x, y = self.pos
        # map (x,y) to a single integer
        return hash((x, y, self.direction))

    def __str__(self):
        return "(x,y)=" + str(self.pos) + ", " + str(self.direction)

    def generateSuccessor(self, vector):
        """
        Generates a new configuration reached by adding the given vector to the
        current position.
        """
        x, y = self.pos
        dx, dy = vector
        direction = Actions.vectorToDirection(vector)
        if direction == Directions.STOP:
            direction = self.direction # Keep current direction if stopped
        return Configuration((x + dx, y + dy), direction)

class Agent:
    """
    An agent chooses an Action at each choice point, given the current
    GameState.
    """
    def __init__(self, index=0):
        self.index = index

    def getAction(self, state):
        raiseNotDefined()

class Grid:
    """
    A 2D grid of booleans, used to represent walls, food, capsules, etc.
    """
    def __init__(self, width, height, initialValue=False, bitRepresentation=None):
        if initialValue not in [True, False]: raise Exception('Grids can only contain booleans')
        self.width = width
        self.height = height
        self.data = [[initialValue for y in range(height)] for x in range(width)]
        if bitRepresentation:
            self._unpackBits(bitRepresentation)

    def __getitem__(self, i):
        return self.data[i]

    def __setitem__(self, key, item):
        self.data[key] = item

    def __str__(self):
        out = [[str(self.data[x][y])[0] for x in range(self.width)] for y in range(self.height)]
        out.reverse()
        return '\n'.join([''.join(x) for x in out])

    def __eq__(self, other):
        if other == None: return False
        return self.data == other.data

    def __hash__(self):
        # Position-dependent hash of boolean grid
        return hash(str(self))

    def copy(self):
        g = Grid(self.width, self.height)
        g.data = [x[:] for x in self.data]
        return g

    def deepCopy(self):
        return self.copy()

    def shallowCopy(self):
        g = Grid(self.width, self.height)
        g.data = self.data
        return g

    def count(self, item=True):
        return sum([x.count(item) for x in self.data])

    def asList(self, key=True):
        list = []
        for x in range(self.width):
            for y in range(self.height):
                if self[x][y] == key: list.append((x, y))
        return list

    def _packBits(self):
        """
        Returns an image format for this grid.
        """
        bits = [self.data[x][y] for y in range(self.height) for x in range(self.width)]
        return bits

    def _unpackBits(self, bits):
        """
        Fills the grid from an image format.
        """
        for y in range(self.height):
            for x in range(self.width):
                self.data[x][y] = bits.pop(0)

class Actions:
    # Directions
    _directions = {Directions.NORTH: (0, 1),
                   Directions.SOUTH: (0, -1),
                   Directions.EAST:  (1, 0),
                   Directions.WEST:  (-1, 0),
                   Directions.STOP:  (0, 0)}

    _directionsAsList = [(_dir, _vec) for _dir, _vec in list(_directions.items())]

    def getPossibleActions(config, walls):
        possible = []
        x, y = config.getPosition()
        x_int, y_int = int(x + 0.5), int(y + 0.5)

        # In between grid points, all legal moves must be along existing axis
        for dir, (dx, dy) in Actions._directionsAsList:
            next_x = x_int + dx
            next_y = y_int + dy
            if not walls[next_x][next_y]:
                possible.append(dir)

        return possible
    getPossibleActions = staticmethod(getPossibleActions)

    def getLegalNeighbors(pt, walls):
        x, y = pt
        x_int, y_int = int(x + 0.5), int(y + 0.5)
        neighbors = []
        for dir, (dx, dy) in Actions._directionsAsList:
            next_x = x_int + dx
            next_y = y_int + dy
            if not walls[next_x][next_y]:
                neighbors.append((next_x, next_y))
        return neighbors
    getLegalNeighbors = staticmethod(getLegalNeighbors)

    def directionToVector(direction, speed = 1.0):
        dx, dy = Actions._directions[direction]
        return (dx * speed, dy * speed)
    directionToVector = staticmethod(directionToVector)

    def vectorToDirection(vector):
        dx, dy = vector
        if dy > 0:
            return Directions.NORTH
        if dy < 0:
            return Directions.SOUTH
        if dx > 0:
            return Directions.EAST
        if dx < 0:
            return Directions.WEST
        return Directions.STOP
    vectorToDirection = staticmethod(vectorToDirection)

class GameStateData:
    def __init__( self, prevState = None ):
        if prevState != None:
            self.food = prevState.food.shallowCopy()
            self.capsules = prevState.capsules[:]
            self.agentStates = self.copyAgentStates( prevState.agentStates )
            self.layout = prevState.layout
            self._eaten = prevState._eaten[:]
            self.score = prevState.score
            self.scoreChange = prevState.scoreChange
        else:
            self.food = None
            self.capsules = None
            self.agentStates = []
            self._eaten = []
            self.score = 0
            self.scoreChange = 0

        self._foodEaten = None
        self._capsuleEaten = None
        self._agentMoved = None
        self._win = False
        self._lose = False

    def deepCopy( self ):
        state = GameStateData( self )
        state.food = self.food.deepCopy()
        state.layout = self.layout.deepCopy()
        state._agentMoved = self._agentMoved
        state._foodEaten = self._foodEaten
        state._capsuleEaten = self._capsuleEaten
        return state

    def copyAgentStates( self, agentStates ):
        copy = []
        for agentState in agentStates:
            copy.append( agentState.copy() )
        return copy

    def __eq__( self, other ):
        if other == None: return False
        if not self.agentStates == other.agentStates: return False
        if not self.food == other.food: return False
        if not self.capsules == other.capsules: return False
        if not self.score == other.score: return False
        return True

    def __hash__( self ):
        return hash((str(self.agentStates), str(self.food), str(self.capsules), self.score))

    def __str__( self ):
        width, height = self.layout.width, self.layout.height
        map = Grid(width, height)
        if self.food != None:
            for x in range(width):
                for y in range(height):
                    map[x][y] = self.food[x][y]
        out = str(map)
        return out

class Game:
    def __init__( self, agents, display, rules, startingIndex=0, muteAgents=False, catchExceptions=False ):
        self.agentCrashes = False
        self.agents = agents
        self.display = display
        self.rules = rules
        self.startingIndex = startingIndex
        self.gameOver = False
        self.muteAgents = muteAgents
        self.catchExceptions = catchExceptions
        self.moveHistory = []

    def run( self ):
        self.display.initialize(self.state.data)
        self.numMoves = 0
        for i in range(len(self.agents)):
            agent = self.agents[i]
            if ("registerInitialState" in dir(agent)):
                agent.registerInitialState(self.state.deepCopy())

        agentIndex = self.startingIndex
        numAgents = len(self.agents)

        while not self.gameOver:
            agent = self.agents[agentIndex]
            action = agent.getAction(self.state.deepCopy())
            self.moveHistory.append((agentIndex, action))
            self.state = self.state.generateSuccessor(agentIndex, action)
            self.display.update(self.state.data)
            self.rules.process(self.state, self)

            if self.state.isWin() or self.state.isLose():
                self.gameOver = True
            agentIndex = (agentIndex + 1) % numAgents
            self.numMoves += 1

        self.display.finish()
