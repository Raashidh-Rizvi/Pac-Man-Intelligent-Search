# graphicsDisplay.py
# ------------------
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


from graphicsUtils import *
import math, time
from game import Directions

DEFAULT_GRID_SIZE = 30.0
INFO_PANE_HEIGHT = 35
BACKGROUND_COLOR = formatColor(0, 0, 0)
WALL_COLOR = formatColor(0.0/255.0, 51.0/255.0, 255.0/255.0)
FOOD_COLOR = formatColor(1.0, 1.0, 1.0)
PACMAN_COLOR = formatColor(255.0/255.0, 255.0/255.0, 61.0/255.0)

class InfoPane:
    def __init__(self, layout, gridsize):
        self.gridsize = gridsize
        self.width = layout.width * gridsize
        self.base = (layout.height + 1) * gridsize
        self.height = INFO_PANE_HEIGHT
        self.drawPane()

    def drawPane(self):
        self.scoreText = text((10, self.base + 4), formatColor(1, 1, 1), "Score: 0", font="Helvetica", size=12, style="bold", anchor="nw")

    def updateScore(self, score):
        changeText(self.scoreText, "Score: %d" % score)

class PacmanGraphics:
    def __init__(self, zoom=1.0, frameTime=0.1, capture=False):
        self.zoom = zoom
        self.gridSize = DEFAULT_GRID_SIZE * zoom
        self.frameTime = frameTime
        self.capture = capture

    def initialize(self, state, isBlue=False):
        self.isBlue = isBlue
        self.startGraphics(state.layout)
        self.drawStaticObjects(state)
        self.drawAgentObjects(state)

    def startGraphics(self, layout):
        self.layout = layout
        self.width = layout.width
        self.height = layout.height
        begin_graphics(self.width * self.gridSize, self.height * self.gridSize + INFO_PANE_HEIGHT, BACKGROUND_COLOR, "Pacman")
        self.infoPane = InfoPane(layout, self.gridSize)

    def drawStaticObjects(self, state):
        layout = state.layout
        self.walls = []
        for x in range(layout.width):
            for y in range(layout.height):
                if layout.walls[x][y]:
                    screen_x, screen_y = self.to_screen((x, y))
                    w = polygon([(screen_x - self.gridSize/2, screen_y - self.gridSize/2),
                                 (screen_x + self.gridSize/2, screen_y - self.gridSize/2),
                                 (screen_x + self.gridSize/2, screen_y + self.gridSize/2),
                                 (screen_x - self.gridSize/2, screen_y + self.gridSize/2)],
                                WALL_COLOR, WALL_COLOR)
                    self.walls.append(w)

        self.food = {}
        for x in range(layout.width):
            for y in range(layout.height):
                if state.food[x][y]:
                    screen_x, screen_y = self.to_screen((x, y))
                    f = circle((screen_x, screen_y), 3 * self.zoom, FOOD_COLOR, FOOD_COLOR)
                    self.food[(x, y)] = f

    def drawAgentObjects(self, state):
        self.agentImages = []
        for index, agentState in enumerate(state.agentStates):
            if agentState.isPacman:
                screen_x, screen_y = self.to_screen(agentState.getPosition())
                p = circle((screen_x, screen_y), self.gridSize * 0.4, PACMAN_COLOR, PACMAN_COLOR)
                self.agentImages.append((p, agentState))

    def update(self, state):
        self.infoPane.updateScore(state.score)
        sleep(self.frameTime)

    def finish(self):
        sleep(self.frameTime)

    def to_screen(self, point):
        (x, y) = point
        x = (x + 0.5) * self.gridSize
        y = (self.height - y - 0.5) * self.gridSize
        return (x, y)
