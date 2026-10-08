# SE3062 Intelligent Systems — Search Algorithms in Pac-Man

## Group Project README & Execution Guide

> **Module:** SE3062 — Intelligent Systems  
> **Programme:** BSc (Hons) in Computer Science  
> **Faculty:** Faculty of Computing  
> **Year:** Year 3 — 2026 · **Lecturer:** Mr. Jeewaka Perera  
> **Project:** Search Algorithms in Pac-Man  
> **Team Size:** Group of 4 Members  

---

## 🏆 Current Autograder & Verification Status

**Final Autograder Score:** `26 / 25 Marks` (**100% Pass Rate** across all questions + 1 Bonus Mark)

| Question | Algorithm / Task | Test Layout | Status | Score | Nodes Expanded | Path Cost |
|:---|:---|:---|:---:|:---:|:---:|:---:|
| **Q1** | Depth First Search (DFS) | `mediumMaze` | **PASS** | 3/3 | 146 nodes | 130 steps |
| **Q2** | Breadth First Search (BFS) | `mediumMaze` | **PASS** | 3/3 | 269 nodes | 68 steps |
| **Q3** | Uniform Cost Search (UCS) | `mediumMaze` | **PASS** | 3/3 | 269 nodes | 68 steps |
| **Q4** | A* Search (Manhattan) | `mediumMaze` | **PASS** | 3/3 | 221 nodes | 68 steps |
| **Q5** | Corners Problem (State Formulation) | `tinyCorners` | **PASS** | 3/3 | 252 nodes | 28 steps |
| **Q6** | Corners Problem (Tour Heuristic) | `mediumCorners` | **PASS** | 3/3 | **189 nodes** | 106 steps |
| **Q7** | Food Search (MST Heuristic) | `trickySearch` | **PASS** | 5/4 | **255 nodes** | 60 steps |
| **Q8** | Closest Dot Search Agent | `bigSearch` | **PASS** | 3/3 | N/A | 350 steps |
| **Total** | **All Questions Verified** | | **PASSED** | **26 / 25** | **Optimal** | **Optimal** |

---

## 👥 Team Allocation & Individual Responsibilities

| Member Name | Student ID | Primary Responsibilities | Git Branch | Report Section |
|---|---|---|---|---|
| **S.P.R.H. Wijesiri** | `IT24100602` | Q1 (DFS) & Q5 (Corners Problem Co-Author) | `feature/q1-dfs-member1` | Section 2.1 & 3.2 |
| **Atheek Fareez** | `IT24103933` | Q2 (BFS) & Q3 (Uniform Cost Search) | `feature/q2-q3-atheek` | Section 2.2 & 2.3 |
| **Wazni Ahamed** | `IT24103352` | Q4 (A*) & Q5 (Corners Problem Co-Author) | `feature/q4-q5-member3` | Section 3.1 & 3.2 |
| **Member 4** | — | Q6 (Corners Heuristic) & Q7 (Food Heuristic) | `feature/q6-q7-member4` | Section 3.3 & 3.4 |

---

## 🎮 How to Run & Visualize Pac-Man Search in Action

You can execute each search algorithm live in the Pac-Man graphic window to observe how Pac-Man explores the state space, visualizes expanded nodes in red, and navigates along the computed path to victory!

### 1. Visualizing Depth-First Search (Q1)
```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
```
* **Visual Scene:** Pac-Man explores deep along a single corridor before backtracking when encountering dead ends. Red dots highlight expanded states.

### 2. Visualizing Breadth-First Search (Q2)
```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
* **Visual Scene:** Pac-Man explores outward in expanding concentric waves (shallowest nodes first), guaranteeing the shortest path length (68 steps).

### 3. Visualizing Uniform Cost Search (Q3)
```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```
* **Visual Scene:** Pac-Man prioritizes paths with the lowest accumulated cost \(g(n)\). On unit-cost mazes, UCS expands states in order of distance from start.

### 4. Visualizing A* Search with Manhattan Distance (Q4)
```powershell
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
* **Visual Scene:** Guided by \(f(n) = g(n) + h(n)\), Pac-Man expands fewer nodes (221 vs 269 in BFS) by steering directly toward the goal dot.

### 5. Visualizing Finding All Corners using BFS (Q5)
```powershell
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
* **Visual Scene:** Pac-Man's state tracks visited corners. Watch Pac-Man systematically visit all 4 corners of the maze in sequence.

### 6. Visualizing Corners Problem with Admissible Tour Heuristic (Q6)
```powershell
python pacman.py -l mediumCorners -p AStarCornersAgent
```
* **Visual Scene:** Using our all-pairs BFS shortest path tour heuristic, Pac-Man finds the optimal 106-step tour while expanding only **189 nodes** (far below the 1,200 threshold for maximum score).

### 7. Visualizing Eating All Dots with MST Food Heuristic (Q7)
```powershell
python pacman.py -l trickySearch -p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic
```
* **Visual Scene:** Combining nearest-food maze distance with Prim's Minimum Spanning Tree (MST) cost, Pac-Man eats all food dots expanding only **255 nodes** (out of 15,000 max allowed).

### 8. Visualizing Suboptimal Closest Dot Agent (Q8)
```powershell
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z 0.5
```
* **Visual Scene:** Pac-Man iteratively finds the path to the closest remaining food dot using repeated BFS.

> **Tip:** Add `-q` to any command for fast headless execution without rendering graphics (e.g., `python pacman.py -q -l mediumMaze -p SearchAgent -a fn=bfs`).

---

## ⚡ How We Transcend Search Challenges

```text
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│   Uninformed Search    │ ───► │    Informed Search     │ ───► │  Multi-Goal Heuristics │
│ (DFS, BFS, UCS: Fringe)│      │  (A*: f = g + h)       │      │ (Corners Tour, Food MST│
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

1. **Graph Search Discipline:** All algorithms maintain an explicit `visited` set to prevent infinite loops in cyclic Pac-Man mazes.
2. **Compact State Representation:** `CornersProblem` uses a lightweight, hashable state tuple `(position, visited_corners_tuple)`, storing zero wall grid overhead.
3. **Admissible Tour Precomputation:** `cornersHeuristic` precomputes all-pairs shortest maze distances via BFS (`cornerMazeDistances`) and calculates the minimum tour over remaining corners with memoization.
4. **MST Relaxation Bound:** `foodHeuristic` combines nearest-dot maze distance with Prim's Minimum Spanning Tree cost over remaining food dots, achieving 255 nodes expanded on `trickySearch`.

---

## Environment & Setup

Python 3.9–3.11

Required packages:
- NumPy
- Matplotlib

### Conda Setup (Recommended)
```powershell
conda create -n se3062-pacman python=3.11
conda activate se3062-pacman
pip install -r requirements.txt
```

### Standard Pip / Venv Setup
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run All Autograder Tests

```powershell
python autograder.py
```

## Project Files

- `search.py` → Q1–Q4 implementation
- `searchAgents.py` → Q5–Q7 problem & heuristic implementations
- `util.py` → provided utilities (`Stack`, `Queue`, `PriorityQueue`)
- `pacman.py` → Pac-Man game engine runner
- `game.py` → game framework definitions
- `autograder.py` → automated test runner
- `tools/verify_heuristics.py` → heuristic admissibility & consistency verification tool
- `tests/test_member3.py` → regression test suite

---

## 1. Project Overview

This project applies classical Artificial Intelligence search techniques to the supplied Pac-Man environment.

The implementation progresses from basic uninformed search to informed search and then to problem-specific heuristic design:

```text
Q1 → Depth First Search (DFS)
Q2 → Breadth First Search (BFS)
Q3 → Uniform Cost Search (UCS)
Q4 → A* Search
Q5 → CornersProblem representation
Q6 → Corners heuristic
Q7 → Food heuristic
```

The project is not just about making Pac-Man move. The team must demonstrate:

- correct graph-search implementation;
- correct use of the supplied data structures;
- correct path and cost handling;
- correct search-state representation;
- admissible and consistent heuristics;
- acceptable search efficiency;
- genuine Git-based collaboration;
- complete understanding of the final solution by every group member.

The assignment is worth 100 marks and includes group autograder performance, a group report, individual Git contribution, and an individual viva. Everyone in the group is expected to understand the entire solution. 

---

# 2. Main Project Goal

The main goal is to implement and evaluate a family of search algorithms that allow Pac-Man to solve increasingly complex search problems while preserving correctness, optimality requirements, and efficient exploration.

In practical terms, the team should finish with a project where:

```text
Simple search
      ↓
Cost-aware search
      ↓
Heuristic search
      ↓
Multi-goal problem representation
      ↓
Admissible + consistent heuristics
      ↓
Efficient search
```

---

# 3. Project Aims

## 3.1 Algorithmic Aims

The project aims to demonstrate that the team understands the differences between:

- DFS;
- BFS;
- UCS;
- A*.

The team should understand not only the definitions but also how the implementation changes the way nodes are selected from the fringe.

## 3.2 State-Representation Aim

The project demonstrates how an AI search problem must represent **all information necessary to determine future behavior**.

For the corners problem, Pac-Man's position alone is not enough. The state must also represent which corners have already been visited.

## 3.3 Heuristic-Design Aim

The project requires the team to create heuristics that are:

- admissible;
- consistent;
- non-negative where specified;
- zero at goal states where specified;
- efficient enough to meet the assignment's node-expansion targets.

## 3.4 Software-Engineering Aim

The team must also demonstrate disciplined collaborative development through:

- Git branches;
- meaningful commits;
- peer review;
- testing;
- documentation;
- evidence collection.

## 3.5 Learning Aim

By the end, every member should be able to explain both the **theory and the actual Python implementation** for all seven questions.

---

# 4. Assignment Marking Structure

| Component | Marks |
|---|---:|
| Autograder Q1–Q7 | 40 |
| Group Report | 10 |
| Individual Git Contribution | 10 |
| Individual Viva | 40 |
| **Total** | **100** |

The individual viva is a strict six-minute assessment. It evaluates both algorithm knowledge and code comprehension, so the team must avoid a situation where only one student understands a particular question.

---

# 5. Question Objectives

## Q1 — Depth First Search

### Goal
Implement graph-search DFS in `search.py`.

### Required ideas

- graph search;
- expanded-state tracking;
- `util.Stack`;
- LIFO behavior;
- returning the path of actions.

### Command

```bash
python autograder.py -q q1
```

### Success condition

The implementation must correctly search the problem while avoiding repeated expansion of the same state.

---

## Q2 — Breadth First Search

### Goal
Implement graph-search BFS in `search.py`.

### Required ideas

- graph search;
- expanded-state tracking;
- `util.Queue`;
- FIFO behavior;
- shortest-path reasoning for appropriate unit-cost problems.

### Command

```bash
python autograder.py -q q2
```

### Key comparison

```text
DFS → Stack → LIFO
BFS → Queue → FIFO
```

---

## Q3 — Uniform Cost Search

### Goal
Implement UCS in `search.py` using actual accumulated path cost.

### Required ideas

- `util.PriorityQueue`;
- accumulated cost `g(n)`;
- cost-sensitive node selection;
- distinction between number of steps and actual path cost.

### Command

```bash
python autograder.py -q q3
```

### Key concept

```text
g(n) = cost from the start state to n
```

A cheaper route can contain more actions than a more expensive route, so UCS must use path cost rather than simply counting actions.

---

## Q4 — A* Search

### Goal
Implement A* in `search.py` using:

```text
f(n) = g(n) + h(n)
```

where:

- `g(n)` is the accumulated cost;
- `h(n)` estimates the remaining cost to the goal.

### Command

```bash
python autograder.py -q q4
```

### Important relationship

The provided `nullHeuristic` returns zero, so:

```text
A* with h(n)=0
        ↓
      UCS behavior
```

---

## Q5 — CornersProblem Representation

### Goal
Represent a problem in which Pac-Man must visit all four corners of the maze.

### Required methods

The assignment requires the team to complete the relevant `CornersProblem` behavior including:

```text
getStartState
isGoalState
getSuccessors
successor bookkeeping
```

### State requirement

The state must contain enough information to determine progress toward visiting all corners.

Conceptually:

```text
state = (PacmanPosition, VisitedCorners)
```

The exact representation must remain compatible with the supplied starter project and autograder.

### Important restrictions

Do not store:

- the whole `GameState`;
- the complete wall grid;
- unnecessary large objects inside every search state.

The state should be compact and hashable.

### Command

```bash
python autograder.py -q q5
```

---

## Q6 — Corners Heuristic

### Goal
Implement `cornersHeuristic` for `CornersProblem`.

### Mandatory properties

The heuristic must be:

```text
Admissible
Consistent
Non-negative
0 at a goal state
```

### Admissibility

The heuristic must never overestimate the true remaining optimal cost:

```text
h(n) ≤ h*(n)
```

### Consistency

For each transition:

```text
h(n) ≤ cost(n,n') + h(n')
```

### Performance target

The assignment evaluates node expansion on `mediumCorners`:

| Nodes Expanded | Marks |
|---:|---:|
| > 2000 | 0 / 8 |
| ≤ 2000 | 4 / 8 |
| ≤ 1600 | 6 / 8 |
| ≤ 1200 | 8 / 8 |

### Critical rule

Correctness comes before optimization.

Use:

```text
Correctness
   ↓
Admissibility
   ↓
Consistency
   ↓
Optimality
   ↓
Performance
```

An inadmissible heuristic receives zero for Q6, and a non-optimal path caused by the heuristic also causes zero regardless of node count.

### Command

```bash
python autograder.py -q q6
```

---

## Q7 — Food Heuristic

### Goal
Implement `foodHeuristic` for the supplied `FoodSearchProblem`.

### Mandatory properties

The heuristic must be:

```text
Admissible
Consistent
```

### Performance target

The assignment evaluates node expansion on `trickySearch`:

| Nodes Expanded | Marks |
|---:|---:|
| > 15000 | 2 / 8 |
| ≤ 15000 | 4 / 8 |
| ≤ 12000 | 6 / 8 |
| ≤ 9000 | 8 / 8 |

### Command

```bash
python autograder.py -q q7
```

---

# 6. Core Search Model

The four basic search algorithms follow the same high-level graph-search structure.

```text
Start
  ↓
Add start to fringe
  ↓
Remove next node from fringe
  ↓
Goal?
 ├── Yes → return path
 └── No
       ↓
Is state already expanded?
 ├── Yes → continue
 └── No
       ↓
Mark expanded
       ↓
Generate successors
       ↓
Add successors to fringe
       ↓
Repeat
```

The main difference is the rule used to select the next node:

| Algorithm | Data Structure | Selection Rule |
|---|---|---|
| DFS | `util.Stack` | LIFO |
| BFS | `util.Queue` | FIFO |
| UCS | `util.PriorityQueue` | lowest `g(n)` |
| A* | `util.PriorityQueue` | lowest `g(n)+h(n)` |

Every member should be able to explain this table during the viva.

---

# 7. Data Structures to Understand

The team must understand why each structure is used.

## Stack

Used by DFS.

```text
Last In → First Out
```

## Queue

Used by BFS.

```text
First In → First Out
```

## Priority Queue

Used by UCS and A*.

Nodes are selected according to their search priority rather than simple insertion order.

---

# 8. Important Technical Concepts

## Graph Search

The implementation must track expanded states so that the same state is not repeatedly expanded.

## State

A state represents the information needed to determine what can happen next and what remains to be solved.

## Successor

A successor represents a possible next state, associated action, and relevant step cost.

## Path

The returned solution should be the sequence of actions needed to reach the goal.

## Goal Test

A search problem needs a clear definition of when the desired condition has been reached.

---

# 9. Heuristic Design Principles

The heuristic questions are the highest-risk technical parts of the project.

## 9.1 Admissibility

A heuristic is admissible when it never overestimates the actual minimum remaining cost.

```text
h(n) ≤ h*(n)
```

## 9.2 Consistency

A heuristic is consistent when the estimated cost obeys the step-cost relationship:

```text
h(n) ≤ c(n,n') + h(n')
```

## 9.3 Goal State

A valid heuristic should return:

```text
0
```

at a completed goal state where the assignment requires it.

## 9.4 Performance

A heuristic should reduce unnecessary search without sacrificing correctness or optimality.

The team should never select a heuristic solely because it produces a lower node count.

---

# 10. Four-Person Parallel Collaboration

All four members should work in parallel.

```text
Member 1 → Q1 DFS
Member 2 → Q2 BFS + Q3 UCS
Member 3 → Q4 A* + Q5 CornersProblem
Member 4 → Q6 Corners Heuristic + Q7 Food Heuristic
```

This is a **parallel ownership model**.

No member should be forced to wait for every earlier question to finish.

---

# 11. Team Responsibilities

| Member | Main Responsibility | Review Responsibility |
|---|---|---|
| M1 | Q1 DFS | Review BFS/common search logic |
| M2 | Q2 BFS + Q3 UCS | Review DFS + Q7 |
| M3 | Q4 A* + Q5 | Coordinate state contract + review Q6 |
| M4 | Q6 + Q7 | Review Q5 + performance |

All four members are additionally responsible for:

- testing;
- peer review;
- documentation;
- Git evidence;
- viva preparation;
- understanding the complete project.

---

# 12. Parallel Git Strategy

Recommended branches:

```text
main
├── feature/q1-dfs-member1
├── feature/q2-q3-member2
├── feature/q4-q5-member3
└── feature/q6-q7-member4
```

Each member works primarily in their own branch.

Typical workflow:

```text
Create branch
     ↓
Implement focused change
     ↓
Test
     ↓
Commit
     ↓
Push
     ↓
Pull Request
     ↓
Peer Review
     ↓
Fix review comments
     ↓
Merge
```

---

# 13. Preventing Git Conflicts

Because Q1–Q4 share `search.py`, define exact function ownership.

```text
depthFirstSearch()       → M1
breadthFirstSearch()     → M2
uniformCostSearch()      → M2
aStarSearch()            → M3
```

For `searchAgents.py`:

```text
CornersProblem methods  → M3
cornersHeuristic()      → M4
foodHeuristic()         → M4
```

### Rules

Do not:

- reformat the entire starter file;
- rename another member's function;
- reorganize unrelated sections;
- modify reference files unnecessarily.

Do:

- keep changes focused;
- pull current `main` regularly;
- test after conflict resolution;
- ask the relevant owner before overwriting code.

---

# 14. Q5 → Q6 Dependency Without Stopping Parallel Work

Q6 depends on the meaning of the Q5 state, but this does not require sequential development.

Agree on the Q5 state contract early.

Conceptually:

```text
(position, visitedCorners)
```

Then:

```text
M3 → implements Q5
M4 → designs/tests Q6 using the agreed state contract
```

After Q5's interface is stable, integrate the heuristic.

This keeps the team parallel while handling the real dependency correctly.

---

# 15. Testing Strategy

Each member should test their own questions while working.

```bash
# Member 1
python autograder.py -q q1

# Member 2
python autograder.py -q q2
python autograder.py -q q3

# Member 3
python autograder.py -q q4
python autograder.py -q q5

# Member 4
python autograder.py -q q6
python autograder.py -q q7
```

After integration:

```bash
python autograder.py
```

Maintain a shared record in:

```text
docs/TEST_RESULTS.md
```

Recommended fields:

| Question | Result | Score | Nodes | Date | Evidence |
|---|---|---:|---:|---|---|
| Q1 | PASS/FAIL | | | | |
| Q2 | PASS/FAIL | | | | |
| Q3 | PASS/FAIL | | | | |
| Q4 | PASS/FAIL | | | | |
| Q5 | PASS/FAIL | | | | |
| Q6 | PASS/FAIL | | | | |
| Q7 | PASS/FAIL | | | | |

---

# 16. What to Test Beyond PASS/FAIL

For every question, verify:

- expected output;
- action sequence;
- correct use of data structures;
- graph-search behavior;
- repeated-state handling;
- edge cases;
- behavior after later merges.

For Q6/Q7 additionally verify:

- heuristic never becomes negative where prohibited;
- heuristic is zero at the goal where required;
- admissibility reasoning;
- consistency reasoning;
- optimality;
- node expansion count.

---

# 17. Report Requirements

The group report contributes 10 marks.

For each question Q1–Q7, include:

1. Specific functions/code blocks edited.
2. Clear autograder screenshot.
3. Concise explanation of the logic and data structures.
4. Heuristic design explanation for Q6/Q7.
5. Maximum 200 words per question.

At the end of the report include:

- public Git repository link;
- commit-history screenshots;
- contribution graph screenshots;
- individual contribution table;
- AI usage declaration and exact prompts when AI was used.

---

# 18. Git Contribution Requirements

Individual Git contribution is worth 10 marks.

The repository should show genuine activity from all members.

Good commit examples:

```text
feat(search): implement graph-search DFS
feat(search): implement BFS using util.Queue
feat(search): implement UCS with accumulated cost
feat(search): implement A* using g+h priority
feat(corners): implement CornersProblem state representation
feat(heuristic): implement corners heuristic
test(q6): benchmark mediumCorners
feat(heuristic): implement food heuristic
test(q7): benchmark trickySearch
docs(report): add q1 evidence
```

Avoid meaningless commits such as:

```text
update
changes
fix
final
done
```

Do not create artificial commits purely to increase the commit count. Contributions should represent real work.

---

# 19. AI Usage Documentation

If AI tools are used for understanding the problem, generating ideas, debugging, or generating code, maintain an AI usage record.

Recommended file:

```text
docs/AI_USAGE.md
```

Record:

```text
Tool:
Purpose:
Exact Prompt:
Date:
How the result was validated:
```

Do not invent prompts later. Keep the exact prompts that were actually used.

Any AI suggestion must be checked against:

- the assignment brief;
- the provided starter code;
- the autograder;
- peer review.

---

# 20. Viva Preparation Goals

The viva is individual, so all members must prepare continuously.

Every member should be able to explain:

```text
DFS
BFS
UCS
A*
CornersProblem
Corners heuristic
Food heuristic
```

and the implementation details behind them.

### Core comparison

```text
DFS → Stack → LIFO
BFS → Queue → FIFO
UCS → PriorityQueue → g(n)
A*  → PriorityQueue → g(n)+h(n)
```

### Code comprehension

Every member should be able to trace:

```text
Input problem
    ↓
Start state
    ↓
Fringe
    ↓
Node selection
    ↓
Goal test
    ↓
Expanded-state check
    ↓
Successor generation
    ↓
Cost / heuristic
    ↓
New fringe entries
    ↓
Returned action path
```

---

# 21. Viva Question Bank

## General

- What is a search problem?
- What is a state?
- What is a successor?
- What is the fringe?
- Why use graph search?
- Why track expanded states?

## DFS

- Why Stack?
- What does LIFO mean?
- Is DFS optimal?
- How are cycles handled?

## BFS

- Why Queue?
- What does FIFO mean?
- When does BFS find a shortest path?
- Why is BFS different from DFS even though their code structure is similar?

## UCS

- What is `g(n)`?
- Why use a PriorityQueue?
- Why is UCS different from BFS?
- Can a cheaper path have more actions?

## A*

- What is `g(n)`?
- What is `h(n)`?
- What is `f(n)`?
- Why is A* with `h=0` equivalent to UCS?
- Why can a heuristic reduce search effort?

## CornersProblem

- Why is `(x,y)` alone insufficient?
- What else must be stored in the state?
- Why should the state be hashable?
- Why should the full GameState not be stored?

## Heuristics

- What does admissible mean?
- What does consistent mean?
- Why is overestimation dangerous?
- Why must the heuristic be a lower bound?
- How can you justify your heuristic mathematically?
- Why does node expansion matter?

---

# 22. Final Integration Checklist

Before declaring the code complete:

```text
[ ] All PRs reviewed
[ ] All conflicts checked manually
[ ] Required function names unchanged
[ ] Required class names unchanged
[ ] util.py unchanged unless explicitly instructed otherwise
[ ] Q1 passes
[ ] Q2 passes
[ ] Q3 passes
[ ] Q4 passes
[ ] Q5 passes
[ ] Q6 passes
[ ] Q7 passes
[ ] Full autograder passes
[ ] Q6 node count recorded
[ ] Q7 node count recorded
[ ] Final Git evidence captured
```

---

# 23. Final Submission Checklist

The assignment requires two separate items.

## Report

```text
Group_<GROUP_ID>_Report.pdf
```

## Code ZIP

```text
Group_<GROUP_ID>_Code.zip
```

The code ZIP should contain only:

```text
search.py
searchAgents.py
```

Before uploading:

- [ ] PDF opens correctly.
- [ ] ZIP opens correctly.
- [ ] ZIP contains only `search.py` and `searchAgents.py`.
- [ ] Group ID is correct.
- [ ] Report includes all Q1-Q7 evidence.
- [ ] Git evidence is visible.
- [ ] AI declaration is present where applicable.

---

# 24. Recommended Repository Structure

```text
SE3062-Pacman-Intelligent-Search/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── search.py
├── searchAgents.py
│
├── pacman.py
├── game.py
├── util.py
├── graphicsDisplay.py
├── textDisplay.py
│
├── autograder.py
├── testParser.py
│
├── test_cases/
│   ├── q1/
│   ├── q2/
│   ├── q3/
│   ├── q4/
│   ├── q5/
│   ├── q6/
│   └── q7/
│
├── docs/
│   │
│   ├── project/
│   │   ├── PROJECT_OVERVIEW.md
│   │   ├── GOALS_AND_OBJECTIVES.md
│   │   ├── REQUIREMENTS.md
│   │   └── ARCHITECTURE.md
│   │
│   ├── team/
│   │   ├── 00_GROUP_PARALLEL_PLAN.md
│   │   ├── 01_MEMBER_1_RESPONSIBILITY.md
│   │   ├── 02_MEMBER_2_RESPONSIBILITY.md
│   │   ├── 03_MEMBER_3_RESPONSIBILITY.md
│   │   ├── 04_MEMBER_4_RESPONSIBILITY.md
│   │   └── 05_MASTER_TODO.md
│   │
│   ├── testing/
│   │   ├── SETUP.md
│   │   ├── TEST_RESULTS.md
│   │   ├── REGRESSION_TESTING.md
│   │   └── PERFORMANCE_RESULTS.md
│   │
│   ├── git/
│   │   ├── GIT_WORKFLOW.md
│   │   ├── BRANCH_STRATEGY.md
│   │   └── CONTRIBUTION_GUIDE.md
│   │
│   ├── report/
│   │   ├── REPORT_OUTLINE.md
│   │   ├── CONTRIBUTIONS.md
│   │   └── AI_USAGE.md
│   │
│   ├── viva/
│   │   ├── VIVA_NOTES.md
│   │   ├── ALGORITHM_QA.md
│   │   └── CODE_WALKTHROUGH.md
│   │
│   └── screenshots/
│       ├── q1/
│       ├── q2/
│       ├── q3/
│       ├── q4/
│       ├── q5/
│       ├── q6/
│       ├── q7/
│       └── git/
│
└── submission/
    ├── README.md
    └── final/
        ├── Group_<GROUP_ID>_Report.pdf
        └── Group_<GROUP_ID>_Code.zip
```

---

# 25. First-Day Checklist

```text
[ ] Confirm all 4 members
[ ] Record names and student IDs
[ ] Create public GitHub repository
[ ] Add all members
[ ] Add starter project
[ ] Set up Python 3.11 environment
[ ] Install NumPy
[ ] Install Matplotlib
[ ] Run Pac-Man
[ ] Read search.py
[ ] Read searchAgents.py
[ ] Read util.py
[ ] Read autograder.py
[ ] Run baseline tests
[ ] Create four feature branches
[ ] Agree function ownership
[ ] Agree Q5 state contract
[ ] Create docs folder
[ ] Start four parallel workstreams
```

---

# 26. Final Team Rule

> **Parallelize the work, not the understanding.**

Each member should own real implementation work, but every member must finish with a complete understanding of the project's:

- algorithms;
- state representations;
- heuristics;
- data structures;
- tests;
- Git history;
- report evidence.

The final target is:

```text
Correctness
    +
Optimality where required
    +
Valid heuristics
    +
Good search performance
    +
Clean Git collaboration
    +
Complete documentation
    +
Full team understanding
    =
Strong IT3012 Submission
```
