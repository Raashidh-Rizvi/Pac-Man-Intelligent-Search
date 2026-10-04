#!/usr/bin/env python3
"""
Root launcher — delegates to src/pacman.py so that
`python pacman.py [options]` works from the project root.
"""
import sys, os

# Ensure the src/ directory is on the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from pacman import readCommand, runGames  # noqa: E402
if __name__ == "__main__":
    args = readCommand(sys.argv[1:])
    runGames(**args)
