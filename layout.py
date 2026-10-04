# layout.py
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


from game import Grid
import os
import random

VISIBILITY_MATRIX_CACHE = {}

class Layout:
    """
    A Layout manages the static information about the game board.
    """

    def __init__(self, layoutText):
        self.width = len(layoutText[0])
        self.height = len(layoutText)
        self.walls = Grid(self.width, self.height, False)
        self.food = Grid(self.width, self.height, False)
        self.capsules = []
        self.agentPositions = []
        self.numGhosts = 0
        self.processLayoutText(layoutText)
        self.layoutText = layoutText

    def getNumGhosts(self):
        return self.numGhosts

    def initializeVisibilityMatrix(self):
        global VISIBILITY_MATRIX_CACHE
        if self.layoutText in VISIBILITY_MATRIX_CACHE:
            self.visibility = VISIBILITY_MATRIX_CACHE[self.layoutText]
            return
        self.visibility = Grid(self.width, self.height, False)

    def isWall(self, pt):
        x, col = pt
        return self.walls[x][col]

    def getRandomLegalPosition(self):
        x = random.choice(range(self.width))
        y = random.choice(range(self.height))
        while self.isWall((x, y)):
            x = random.choice(range(self.width))
            y = random.choice(range(self.height))
        return (x, y)

    def getRandomCorner(self):
        poses = [(1, 1), (1, self.height - 2), (self.width - 2, 1), (self.width - 2, self.height - 2)]
        return random.choice(poses)

    def getFurtherCorner(self, pacPos):
        poses = [(1, 1), (1, self.height - 2), (self.width - 2, 1), (self.width - 2, self.height - 2)]
        dists = [abs(pacPos[0] - pos[0]) + abs(pacPos[1] - pos[1]) for pos in poses]
        idx = dists.index(max(dists))
        return poses[idx]

    def processLayoutText(self, layoutText):
        """
        Coordinates are (x, y) with (0, 0) at the bottom left.
        """
        maxY = self.height - 1
        for y in range(self.height):
            for x in range(self.width):
                layoutChar = layoutText[maxY - y][x]
                self.processLayoutChar(x, y, layoutChar)
        self.agentPositions.sort()
        self.agentPositions = [ ( i == 0, pos ) for i, pos in self.agentPositions ]

    def processLayoutChar(self, x, y, layoutChar):
        if layoutChar == '%':
            self.walls[x][y] = True
        elif layoutChar == '.':
            self.food[x][y] = True
        elif layoutChar == 'o':
            self.capsules.append((x, y))
        elif layoutChar == 'P':
            self.agentPositions.append( (0, (x, y)) )
        elif layoutChar in ['1', '2', '3', '4']:
            self.agentPositions.append( (int(layoutChar), (x,y)) )
            self.numGhosts += 1

    def deepCopy(self):
        return Layout(self.layoutText[:])

    def __str__(self):
        return "\n".join(self.layoutText)

def getLayout(name, back = 2):
    if name.endswith('.lay'):
        layout = tryToLoad(name)
        if layout == None: layout = tryToLoad(os.path.join('layouts', name))
    else:
        layout = tryToLoad(name + '.lay')
        if layout == None: layout = tryToLoad(os.path.join('layouts', name + '.lay'))

    return layout

def tryToLoad(fullname):
    if not os.path.exists(fullname): return None
    f = open(fullname)
    try: return Layout([line.strip() for line in f])
    finally: f.close()
