#!/usr/bin/env python3
"""
Root launcher — delegates to src/autograder.py so that
`python autograder.py [-q qN]` works from the project root.
"""
import sys, os

# Ensure the src/ directory is on the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from autograder import readCommand, runQuestion, runAll  # noqa: E402
if __name__ == "__main__":
    options = readCommand(sys.argv[1:])
    if options.question:
        runQuestion(options.question)
    else:
        runAll()
