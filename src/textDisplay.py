# textDisplay.py
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


import time

class NullGraphics:
    def initialize(self, state, isBlue = False):
        pass

    def update(self, state):
        pass

    def checkNullDisplay(self):
        return True

    def finish(self):
        pass

class PacmanGraphics:
    def __init__(self, speed=None):
        if speed != None:
            self.speed = speed
        else:
            self.speed = 0.1

    def initialize(self, state, isBlue = False):
        self.draw(state)
        self.pause()

    def update(self, state):
        self.draw(state)
        self.pause()

    def pause(self):
        time.sleep(self.speed)

    def draw(self, state):
        print(state)

    def finish(self):
        pass
