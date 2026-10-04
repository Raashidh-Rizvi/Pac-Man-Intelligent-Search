# testClasses.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

import sys

class Question:
    def __init__(self, questionDict, maxPoints):
        self.questionDict = questionDict
        self.maxPoints = maxPoints
        self.testCases = []

    def addTestCase(self, testCase, points):
        self.testCases.append((testCase, points))

    def execute(self, grades):
        grades.currentQuestion = self.questionDict.get('name', 'Question')
        grades.maxes[grades.currentQuestion] = self.maxPoints
        passed = True
        for testCase, points in self.testCases:
            if not testCase.execute(grades):
                passed = False
        if passed:
            grades.setPoints(self.maxPoints)

class TestCase:
    def __init__(self, question, testDict):
        self.question = question
        self.testDict = testDict
        self.path = testDict.get('path', '')

    def execute(self, grades):
        return True
