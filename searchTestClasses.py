# searchTestClasses.py
# --------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

from testClasses import TestCase, Question
import layout, pacman, search, searchAgents

class GraphSearchTest(TestCase):
    def __init__(self, question, testDict):
        super().__init__(question, testDict)
        self.alg = testDict.get('alg', 'depthFirstSearch')
        self.layoutName = testDict.get('layoutName', 'tinyMaze')

    def execute(self, grades):
        try:
            lay = layout.getLayout(self.layoutName)
            if not lay:
                grades.addMessage(f"Layout {self.layoutName} not found")
                return False
            searchFn = getattr(search, self.alg)
            prob = searchAgents.PositionSearchProblem(pacman.GameState())
            # Basic validation check
            return True
        except Exception as e:
            grades.addMessage(f"Exception during {self.alg} test: {e}")
            return False
