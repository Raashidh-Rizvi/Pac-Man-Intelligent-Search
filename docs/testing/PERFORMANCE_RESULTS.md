# Algorithm Performance Results

## Node Expansion Comparison Table

| Algorithm / Heuristic | Layout | Total Cost | Expanded Nodes | Autograder Max Threshold |
|---|---|---|---|---|
| DFS | mediumMaze | - | - | - |
| BFS | mediumMaze | - | - | - |
| UCS | mediumMaze | - | - | - |
| A* (Manhattan) | mediumMaze | - | - | - |
| Corners Problem (BFS) | mediumCorners | 42 | 684 | - |
| Corners Heuristic (A*) | mediumCorners | 42 | **42** | < 1200 nodes |
| Food Heuristic (A*) | trickySearch | - | - | < 7000 nodes |

---

## Q6 — Corners Heuristic Evidence (Member 4)

Measured 2026-10-07 on the layouts currently in `src/layouts/`.

| Search | Layout | Cost | Expanded |
|---|---|---|---|
| BFS (Q5 baseline) | tinyCorners | 11 | 114 |
| A* + `nullHeuristic` (= UCS) | tinyCorners | 11 | 114 |
| A* + `cornersHeuristic` | tinyCorners | 11 | **11** |
| BFS (Q5 baseline) | mediumCorners | 42 | 684 |
| A* + `nullHeuristic` (= UCS) | mediumCorners | 42 | 684 |
| A* + `cornersHeuristic` | mediumCorners | 42 | **42** |

Expansions drop 684 -> 42 (a 16.3x reduction) while the path cost stays at the
optimum of 42, so the heuristic preserves optimality. Expanded nodes equal the
path cost, meaning A* expanded essentially only nodes along an optimal path --
the heuristic is exact at the start state (h = h* = 42).

Reproduce with:

```bash
python autograder.py -q q6
python pacman.py -l mediumCorners -p AStarCornersAgent -q    # from src/
```

### Admissibility and consistency: verified, not assumed

Both properties were checked exhaustively rather than argued informally. The
checker enumerates every reachable state, computes the true cost-to-go h* by a
reverse breadth-first sweep from the goal states, then asserts h <= h* on every
state and h(s) <= c(s,s') + h(s') on every edge.

| Layout | States checked | Admissible | h(goal) = 0 | Consistent |
|---|---|---|---|---|
| tinyCorners | 196 | YES | YES | YES |
| mediumCorners | 1221 | YES | YES | YES |

The previous greedy nearest-corner implementation failed this check with 20
admissibility and 18 consistency violations on mediumCorners. Worst case was
state `((9,5), (False,True,False,False))`, where it returned 42 against a true
cost-to-go of 34, because chaining to the nearest corner commits to a visiting
order whose total can exceed the optimal tour.

> Caveat: `mediumCorners.lay` in this repo is an 18x13 reconstruction with an
> optimal cost of 42. The official layout is 35x13 with an optimal cost of 106,
> which is what the < 1200 node threshold is calibrated against. These numbers
> are internally consistent but are not directly comparable to the mark scheme
> until the official layouts are restored.
