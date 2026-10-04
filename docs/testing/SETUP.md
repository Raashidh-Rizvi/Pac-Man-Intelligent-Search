# Environment & Testing Setup Guide

For full installation and environment configuration guidelines, see [SETUP.md](../SETUP.md).

## Quick Execution Summary

### Run Full Autograder
```powershell
python autograder.py
```

### Run Individual Question Autograder
```powershell
python autograder.py -q q1
python autograder.py -q q2
python autograder.py -q q3
python autograder.py -q q4
python autograder.py -q q5
python autograder.py -q q6
python autograder.py -q q7
```

### Visual Pac-Man Agent Testing
```powershell
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=ucs
python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
