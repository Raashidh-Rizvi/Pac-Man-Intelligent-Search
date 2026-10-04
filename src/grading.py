# grading.py
# ----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

import sys
import traceback
from collections import defaultdict

class Grades:
    def __init__(self, projectParams, maxPoints=100):
        self.points = defaultdict(int)
        self.maxes = defaultdict(int)
        self.messages = defaultdict(list)
        self.projectParams = projectParams
        self.maxPoints = maxPoints
        self.currentQuestion = None

    def addPoints(self, amt):
        self.points[self.currentQuestion] += amt

    def setPoints(self, amt):
        self.points[self.currentQuestion] = amt

    def assignZero(self):
        self.points[self.currentQuestion] = 0

    def addMessage(self, msg):
        self.messages[self.currentQuestion].append(msg)

    def fail(self, msg):
        self.addMessage(msg)
        self.assignZero()

    def produceOutput(self):
        print("=== AUTOGRADER SUMMARY ===")
        total_score = 0
        max_total = 0
        for q, p in self.points.items():
            m = self.maxes[q]
            print(f"Question {q}: {p}/{m} points")
            total_score += p
            max_total += m
        print(f"Total Score: {total_score}/{max_total}")
