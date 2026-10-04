# pacman.py
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
Pacman.py holds the logic for the classic Pacman game along with the main
code to run a game.
"""
from game import GameStateData
from game import Game
from game import Directions
from game import Actions
from game import Configuration
from util import nearestPoint
from util import manhattanDistance
import util, layout, sys, os, random

# ---------------------------------------------------------------------------
# KeyboardAgent – lets a human player control Pac-Man via arrow keys / WASD.
# ---------------------------------------------------------------------------
from game import Agent, Directions

PACMAN_MOVE_NORTH = {'Up', 'w', 'W'}
PACMAN_MOVE_SOUTH = {'Down', 's', 'S'}
PACMAN_MOVE_EAST  = {'Right', 'd', 'D'}
PACMAN_MOVE_WEST  = {'Left', 'a', 'A'}
PACMAN_STOP       = {'space', 'q', 'Q'}

class KeyboardAgent(Agent):
    """
    An agent controlled by keyboard or UI buttons at the bottom of the screen.
    Click BFS, DFS, UCS, or A* Search to execute automated search paths,
    or use Arrow keys / WASD to move manually.
    """
    def __init__(self, index=0):
        super().__init__(index)
        self.lastMove = Directions.STOP
        self.keys = set()
        self.planned_actions = []
        self.autoAlgo = None    # algorithm that keeps replanning until all food is eaten

    def getAction(self, state):
        from graphicsUtils import get_clicked_algo, keys_waiting, keys_pressed
        import graphicsUtils as _gu

        # Pump the Tkinter event queue so key/button events are processed
        try:
            if _gu._root_window is not None:
                _gu._root_window.update()
        except Exception:
            pass

        # Check if an algorithm button was clicked at the bottom toolbar
        clicked_algo = get_clicked_algo()
        if clicked_algo is not None:
            self.autoAlgo = clicked_algo
            self.planned_actions = self.planPath(clicked_algo, state)
            # Drop any held/remembered key so it doesn't override or follow the plan
            keys_waiting()
            self.keys = set()
            self.lastMove = Directions.STOP

        # A new key press hands control back to the player
        newKeys = set(keys_waiting())
        keys = newKeys | set(keys_pressed())
        if newKeys and self.autoAlgo is not None:
            self.autoAlgo = None
            self.planned_actions = []

        # Path finished but dots remain: search again for the next one
        if not self.planned_actions and self.autoAlgo is not None:
            self.planned_actions = self.planPath(self.autoAlgo, state)
            if not self.planned_actions:
                self.autoAlgo = None

        # If we have planned actions from an algorithm click, execute them sequentially!
        if self.planned_actions:
            move = self.planned_actions.pop(0)
            if move in state.getLegalPacmanActions():
                self.lastMove = move if self.planned_actions else Directions.STOP
                return move
            self.planned_actions = []

        if keys:
            self.keys = keys

        legal = state.getLegalPacmanActions()
        move = self.getMove(self.keys)

        if move == Directions.STOP:
            # Try the last successful direction (smoother experience)
            if self.lastMove in legal:
                move = self.lastMove

        if move not in legal:
            move = Directions.STOP

        self.lastMove = move
        return move

    def planPath(self, algo, state):
        """Run the chosen search from Pac-Man's position to the target food dot."""
        import search
        from searchAgents import PositionSearchProblem, manhattanHeuristic
        if state.getNumFood() == 0:
            return []
        problem = PositionSearchProblem(state, warn=False)
        if algo == 'bfs':
            actions = search.bfs(problem)
        elif algo == 'dfs':
            actions = search.dfs(problem)
        elif algo == 'ucs':
            actions = search.ucs(problem)
        elif algo == 'astar':
            actions = search.aStarSearch(problem, manhattanHeuristic)
        else:
            return []
        print('[%s] goal %s: path length %d, cost %d, nodes expanded %d' % (
            algo.upper(), problem.goal, len(actions), problem.getCostOfActions(actions), problem._expanded))
        return list(actions)

    def getMove(self, keys):
        if keys & PACMAN_MOVE_NORTH:
            return Directions.NORTH
        if keys & PACMAN_MOVE_SOUTH:
            return Directions.SOUTH
        if keys & PACMAN_MOVE_EAST:
            return Directions.EAST
        if keys & PACMAN_MOVE_WEST:
            return Directions.WEST
        return Directions.STOP

# ---------------------------------------------------------------------------

class AgentState:
    """
    AgentStates hold the state of an agent (position, direction, etc).
    """
    def __init__( self, startConfiguration, isPacman ):
        self.start = startConfiguration
        self.configuration = startConfiguration
        self.isPacman = isPacman
        self.scaredTimer = 0

    def copy( self ):
        state = AgentState( self.start, self.isPacman )
        state.configuration = self.configuration
        state.scaredTimer = self.scaredTimer
        return state

    def getPosition(self):
        if self.configuration == None: return None
        return self.configuration.getPosition()

    def getDirection(self):
        return self.configuration.getDirection()

class GameState:
    """
    A GameState specifies the full game state, including the food, capsules,
    agent configurations and score changes.
    """

    def __init__( self, prevState = None ):
        if prevState != None:
            self.data = GameStateData(prevState.data)
        else:
            self.data = GameStateData()

    def getLegalActions( self, agentIndex=0 ):
        if self.isWin() or self.isLose(): return []
        if agentIndex == 0:  # Pacman
            return PacmanRules.getLegalActions( self )
        else:
            return GhostRules.getLegalActions( self, agentIndex )

    def generateSuccessor( self, agentIndex, action ):
        # Check that we're not in a response state
        if self.isWin() or self.isLose(): raise Exception('Can\'t generate a successor of a terminal state.')

        # Copy current state
        state = GameState(self)

        # Developer API for generating successor
        if agentIndex == 0: # Pacman
            state.data._eaten = [False for i in range(state.getNumAgents())]
            PacmanRules.applyAction( state, action )
        else:
            GhostRules.applyAction( state, action, agentIndex )

        if agentIndex == 0:
            state.data.scoreChange = -1 # Time penalty
        else:
            GhostRules.decrementTimer( state.data.agentStates[agentIndex] )

        GhostRules.checkDeath( state, agentIndex )

        state.data._agentMoved = agentIndex
        state.data.score += state.data.scoreChange
        return state

    def getLegalPacmanActions( self ):
        return self.getLegalActions( 0 )

    def generatePacmanSuccessor( self, action ):
        return self.generateSuccessor( 0, action )

    def getPacmanState( self ):
        return self.data.agentStates[0].copy()

    def getPacmanPosition( self ):
        return self.data.agentStates[0].getPosition()

    def getGhostStates( self ):
        return [ state.copy() for state in self.data.agentStates[1:] ]

    def getGhostState( self, agentIndex ):
        if agentIndex == 0 or agentIndex >= self.getNumAgents():
            raise Exception("Invalid index passed to getGhostState")
        return self.data.agentStates[agentIndex].copy()

    def getGhostPosition( self, agentIndex ):
        if agentIndex == 0:
            raise Exception("Pacman's index passed to getGhostPosition")
        return self.data.agentStates[agentIndex].getPosition()

    def getGhostPositions(self):
        return [s.getPosition() for s in self.data.agentStates[1:]]

    def getNumAgents( self ):
        return len( self.data.agentStates )

    def getScore( self ):
        return float(self.data.score)

    def getCapsules(self):
        return self.data.capsules

    def getNumFood( self ):
        return self.data.food.count()

    def getFood(self):
        return self.data.food

    def getWalls(self):
        return self.data.layout.walls

    def hasFood(self, x, y):
        return self.data.food[x][y]

    def hasWall(self, x, y):
        return self.data.layout.walls[x][y]

    def isWin( self ):
        return self.data._win

    def isLose( self ):
        return self.data._lose

    def deepCopy( self ):
        state = GameState( self )
        state.data = self.data.deepCopy()
        return state

    def __eq__( self, other ):
        if other == None: return False
        return self.data == other.data

    def __hash__( self ):
        return hash( self.data )

    def __str__( self ):
        return str(self.data)

    def initialize( self, layout, numGhostAgents=0 ):
        self.data.initialize(layout, numGhostAgents)

class GameStateData(GameStateData):
    def initialize( self, layout, numGhostAgents ):
        self.food = layout.food.copy()
        self.capsules = layout.capsules[:]
        self.layout = layout
        self.score = 0
        self.scoreChange = 0

        self.agentStates = []
        numGhosts = 0
        for isPacman, pos in layout.agentPositions:
            if not isPacman:
                if numGhosts < numGhostAgents:
                    numGhosts += 1
                else:
                    continue
            self.agentStates.append( AgentState( Configuration( pos, Directions.STOP ), isPacman ) )
        self._eaten = [False for a in self.agentStates]

import game

class PacmanRules:
    PACMAN_SPEED=1

    def getLegalActions( state ):
        return Actions.getPossibleActions( state.getPacmanState().configuration, state.getWalls() )
    getLegalActions = staticmethod( getLegalActions )

    def applyAction( state, action ):
        legal = PacmanRules.getLegalActions( state )
        if action not in legal:
            raise Exception("Illegal action " + str(action))

        pacmanState = state.data.agentStates[0]

        # Update Configuration
        vector = Actions.directionToVector( action, PacmanRules.PACMAN_SPEED )
        pacmanState.configuration = pacmanState.configuration.generateSuccessor( vector )

        # Eat food
        next = pacmanState.configuration.getPosition()
        nearest = nearestPoint( next )
        if manhattanDistance( nearest, next ) <= 0.5:
            # Remove food
            PacmanRules.consume( nearest, state )
    applyAction = staticmethod( applyAction )

    def consume( position, state ):
        x,y = position

        # Eat food
        if state.data.food[x][y]:
            state.data.scoreChange += 10
            state.data.food[x][y] = False
            state.data._foodEaten = position
            if state.getNumFood() == 0:
                state.data._win = True

        # Eat capsule
        if position in state.getCapsules():
            state.data.capsules.remove( position )
            state.data._capsuleEaten = position
            for ghostState in state.getGhostStates():
                ghostState.scaredTimer = 40
    consume = staticmethod( consume )

    def process( state, game ):
        """
        Called by Game.run() after every agent move.
        All game logic (action application, death checks, scoring) is already
        handled inside GameState.generateSuccessor(), so this is a no-op.
        """
        pass
    process = staticmethod( process )

class GhostRules:
    GHOST_SPEED=1.0

    def getLegalActions( state, ghostIndex ):
        conf = state.getGhostState( ghostIndex ).configuration
        return Actions.getPossibleActions( conf, state.getWalls() )
    getLegalActions = staticmethod( getLegalActions )

    def applyAction( state, action, ghostIndex ):
        legal = GhostRules.getLegalActions( state, ghostIndex )
        if action not in legal:
            raise Exception("Illegal ghost action " + str(action))

        ghostState = state.data.agentStates[ghostIndex]
        speed = GhostRules.GHOST_SPEED
        if ghostState.scaredTimer > 0: speed /= 2.0
        vector = Actions.directionToVector( action, speed )
        ghostState.configuration = ghostState.configuration.generateSuccessor( vector )
    applyAction = staticmethod( applyAction )

    def decrementTimer( ghostState ):
        if ghostState.scaredTimer > 0:
            ghostState.scaredTimer -= 1

    decrementTimer = staticmethod( decrementTimer )

    def checkDeath( state, agentIndex ):
        pacmanPosition = state.getPacmanPosition()
        if agentIndex == 0: # Pacman just moved
            for index in range( 1, state.getNumAgents() ):
                ghostState = state.data.agentStates[index]
                ghostPosition = ghostState.configuration.getPosition()
                if GhostRules.canKillPacman( pacmanPosition, ghostPosition ):
                    GhostRules.collide( state, ghostState, index )
        else: # Ghost just moved
            ghostState = state.data.agentStates[agentIndex]
            ghostPosition = ghostState.configuration.getPosition()
            if GhostRules.canKillPacman( pacmanPosition, ghostPosition ):
                GhostRules.collide( state, ghostState, agentIndex )
    checkDeath = staticmethod( checkDeath )

    def collide( state, ghostState, agentIndex ):
        if ghostState.scaredTimer > 0:
            state.data.scoreChange += 200
            ghostState.configuration = ghostState.start
            ghostState.scaredTimer = 0
        else:
            if not state.isWin():
                state.data.scoreChange -= 500
                state.data._lose = True
    collide = staticmethod( collide )

    def canKillPacman( pacmanPosition, ghostPosition ):
        return manhattanDistance( pacmanPosition, ghostPosition ) <= 0.5
    canKillPacman = staticmethod( canKillPacman )

def default(str):
    return str + ' [Default: %default]'

def parseAgentArgs(str):
    if str == None: return {}
    pieces = str.split(',')
    opts = {}
    for p in pieces:
        if '=' in p:
            key, val = p.split('=')
            opts[key] = val
        else:
            opts[p] = True
    return opts

def readCommand( argv ):
    import optparse
    usageStr = """
    USAGE:      python pacman.py [options]
    EXAMPLE:    python pacman.py --layout bigMaze --pacman SearchAgent -a fn=bfs
    """
    parser = optparse.OptionParser(usageStr)

    parser.add_option('-n', '--numGames', dest='numGames', type='int',
                      help=default('the number of GAMES to play'), metavar='GAMES', default=1)
    parser.add_option('-l', '--layout', dest='layout',
                      help=default('the LAYOUT_FILE from which to load the map layout'),
                      metavar='LAYOUT_FILE', default='mediumMaze')
    parser.add_option('-p', '--pacman', dest='pacman',
                      help=default('the agent TYPE in pacmanAgents.py to use'),
                      metavar='TYPE', default='KeyboardAgent')
    parser.add_option('-t', '--textGraphics', action='store_true', dest='textGraphics',
                      help='Display output as text only', default=False)
    parser.add_option('-q', '--quietTextGraphics', action='store_true', dest='quietTextGraphics',
                      help='Generate minimal output and no graphics', default=False)
    parser.add_option('-g', '--ghosts', dest='ghost',
                      help=default('the ghost agent type in ghostAgents.py to use'),
                      metavar='TYPE', default='RandomGhost')
    parser.add_option('-k', '--numGhosts', type='int', dest='numGhosts',
                      help=default('The maximum number of ghosts to use'), default=4)
    parser.add_option('-z', '--zoom', type='float', dest='zoom',
                      help=default('Zoom the size of the graphics window'), default=1.0)
    parser.add_option('-f', '--fixRandomSeed', action='store_true', dest='fixRandomSeed',
                      help='Fixes the random seed to always play the same game', default=False)
    parser.add_option('-r', '--recordActions', action='store_true', dest='record',
                      help='Writes game histories to a file (named game_actions)', default=False)
    parser.add_option('--replay', dest='gameToReplay',
                      help='A recorded game file (e.g. game_actions) to replay', default=None)
    parser.add_option('-a', '--agentArgs', dest='agentArgs',
                      help='Comma separated values sent to agent. e.g. "opt1=val1,opt2=val2"')

    options, otherjunk = parser.parse_args(argv)
    if len(otherjunk) != 0:
        raise Exception('Command line input not understood: ' + str(otherjunk))

    args = {}

    if options.fixRandomSeed: random.seed('cs188')

    # Choose a Layout
    args['layout'] = layout.getLayout( options.layout )
    if args['layout'] == None: raise Exception("The layout " + options.layout + " cannot be found")

    # Choose a Pacman agent
    noKeyboard = options.textGraphics or options.quietTextGraphics
    pacmanType = util.lookup(options.pacman, globals())
    if pacmanType is None:
        import searchAgents
        pacmanType = util.lookup(options.pacman, searchAgents.__dict__)
    if pacmanType is None:
        raise Exception("Pacman agent " + options.pacman + " not found")

    agentOpts = parseAgentArgs(options.agentArgs)
    args['pacman'] = pacmanType(**agentOpts)

    # Choose Ghost agents
    ghostType = util.lookup(options.ghost, globals())
    if ghostType is None:
        import ghostAgents
        ghostType = util.lookup(options.ghost, ghostAgents.__dict__)
    numGhosts = min(options.numGhosts, args['layout'].getNumGhosts())
    args['ghosts'] = [ghostType( i+1 ) for i in range( numGhosts )]

    # Choose a display format
    if options.quietTextGraphics:
        import textDisplay
        args['display'] = textDisplay.NullGraphics()
    elif options.textGraphics:
        import textDisplay
        args['display'] = textDisplay.PacmanGraphics()
    else:
        try:
            import graphicsDisplay
            args['display'] = graphicsDisplay.PacmanGraphics(options.zoom, frameTime = 0.1)
        except Exception:
            import textDisplay
            args['display'] = textDisplay.PacmanGraphics()

    args['numGames'] = options.numGames
    return args

def runGames( layout, pacman, ghosts, display, numGames, record=False ):
    # Hack for namespace
    game.Configuration.layout = layout
    import ghostAgents
    import __main__
    __main__.__dict__['_display'] = display

    rules = PacmanRules()
    games = []

    for i in range( numGames ):
        gameInstance = Game([pacman] + ghosts, display, rules)
        gameInstance.state = GameState()
        gameInstance.state.initialize( layout, len(ghosts) )
        gameInstance.run()
        games.append(gameInstance)

    return games

if __name__ == '__main__':
    """
    The main function called when pacman.py is run from the command line:

    > python pacman.py
    """
    args = readCommand( sys.argv[1:] )
    runGames( **args )
