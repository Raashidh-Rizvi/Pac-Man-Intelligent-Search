# System Architecture

## Core Components
```text
┌─────────────────────────────────────────────────────────────┐
│                      Pac-Man Engine                         │
│                    (pacman.py / game.py)                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
┌───────────────────────┐             ┌───────────────────────┐
│       search.py       │             │    searchAgents.py    │
│  General Search Algo  │             │ Problem & Heuristics  │
│  (DFS, BFS, UCS, A*)  │             │ (Corners & Food)      │
└───────────┬───────────┘             └───────────┬───────────┘
            │                                     │
            └──────────────────┬──────────────────┘
                               ▼
                    ┌───────────────────┐
                    │      util.py      │
                    │  Data Structures  │
                    └───────────────────┘
```

## Abstract Data Flow
1. `SearchProblem` defines `getStartState()`, `isGoalState(state)`, `getSuccessors(state)`, `getCostOfActions(actions)`.
2. General search functions in `search.py` take any `SearchProblem` and return a list of actions `[Directions.NORTH, ...]`.
3. `searchAgents.py` defines state space representations and heuristic evaluation functions `h(state, problem)`.
