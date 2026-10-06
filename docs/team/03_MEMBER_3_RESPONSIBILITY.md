# Member 3 — Responsibility & Task Plan

## Role

**Role:** A* and Search-Problem Modeling Lead  
**Primary Questions:** Q4 — A* Search, Q5 — CornersProblem  
**Primary Files:** `src/search.py`, `src/searchAgents.py`

## Verified baseline and actual contribution (2026-10-07)

A* and CornersProblem already existed at baseline `43e6cde`. Member 3 did
not originally implement them in this execution phase. Both implementations
were preserved after passing the downloaded Berkeley Q4/Q5 tests on Python
3.14.3. Verification on the required Python 3.9–3.11 runtime remains pending.

Actual work: fix SearchAgent's selected-heuristic forwarding, add seven
regression tests, verify the existing Q4/Q5 implementations, document the Q5
contract, and reproduce the Q6 issue for Member 4 without editing heuristics.
See [verification evidence](../testing/MEMBER3_VERIFICATION.md).

---

# 1. Primary Development Work

## Q4 — A* Search

Implement:

```python
aStarSearch(problem, heuristic)
```

Core priority:

```text
f(n) = g(n) + h(n)
```

where:

- `g(n)` = accumulated cost already travelled;
- `h(n)` = estimated remaining cost.

The default `nullHeuristic` is always zero, so A* becomes equivalent to UCS.

### Test

```bash
python autograder.py -q q4
```

## Q5 — CornersProblem

Implement the required methods in `searchAgents.py`:

```text
getStartState
isGoalState
getSuccessors
successor bookkeeping
```

The state must be:

- compact;
- hashable;
- sufficient to represent Pac-Man's location and corner-visit progress;
- free of the full wall grid;
- free of the complete `GameState`.

### Test

```bash
python autograder.py -q q5
```

---

# 2. Q5 State Contract

Coordinate with Member 4 early.

The existing state is exactly:

```text
((x, y), (visited_bottom_left, visited_top_left,
          visited_bottom_right, visited_top_right))
```

Each flag is a boolean. The outer state, position, and visited flags are tuples,
so the state is compact and hashable. The ordering follows `problem.corners`:

| Index | Corner |
|---|---|
| 0 | `(1, 1)` |
| 1 | `(1, walls.height - 2)` |
| 2 | `(walls.width - 2, 1)` |
| 3 | `(walls.width - 2, walls.height - 2)` |

Starting at a corner sets its flag immediately. A successor preserves existing
flags and marks its destination corner using a fresh tuple. Goal states have
all four flags set. Walls are stored on the problem, never inside the state.
Each legal move costs 1; `_expanded` increases once per successor-generation call.

Member 4's `cornersHeuristic` indexes this tuple using the same corner order.
Preserve this interface; agreement with Member 4 is still a coordination task.

This contract allows Member 4 to correct Q6 independently of Q5.

---

# 3. Technical Knowledge Ownership

Member 3 should deeply understand:

- A*;
- `g(n)`;
- `h(n)`;
- `f(n)`;
- priority queues;
- problem-state design;
- hashability;
- corner bookkeeping;
- goal-state definition;
- successor generation.

---

# 4. Secondary Responsibilities

Review Member 4's Q6/Q7 heuristics.

Specifically check:

- whether the heuristic aligns with the actual state representation;
- whether the goal condition is handled correctly;
- admissibility argument;
- consistency argument;
- effect on A* integration.

Also review UCS where it affects A* behavior.

---

# 5. Testing Responsibilities

Primary:

```bash
python autograder.py -q q4
python autograder.py -q q5
```

Integration:

```bash
python autograder.py -q q6
python autograder.py
```

---

# 6. Git Responsibilities

Branch:

```text
feature/q4-q5-member3
```

Recommended commits:

```text
fix(search-agent): forward selected heuristic to A*
docs(q5): document corner-state contract and verification
docs(team): correct Member 3 Q4-Q5 ownership
docs(report): add q4-q5 evidence
```

Use messages only for work actually completed. Do not claim new authorship of
the existing A*/CornersProblem implementations or claim Python 3.11 results
until they have been run. Avoid broad refactoring that creates merge conflicts.

---

# 7. Report Responsibilities

Write:

- Q4 section;
- Q5 section;
- screenshots for Q4 and Q5.

Q5 should explain:

- state representation;
- goal test;
- successor generation;
- corner bookkeeping;
- why the state must be hashable and compact.

Maximum 200 words per question.

---

# 8. Viva Preparation

Be able to explain:

- why A* uses `g+h`;
- why `nullHeuristic` makes A* equivalent to UCS;
- what a search state is;
- why `(x,y)` alone is not enough for CornersProblem;
- why visited-corner information belongs in the state;
- why the full GameState should not be stored in every search state.

Also understand both heuristics well enough to defend them mathematically.

---

# 9. Definition of Done

- [x] Existing Q4 implementation inspected and preserved.
- [x] Existing Q5 implementation inspected and preserved.
- [ ] Q5 state contract agreed with Member 4.
- [x] Berkeley Q4/Q5 tests executed on Python 3.14.3 (see evidence).
- [ ] Q4 verified on required Python 3.9–3.11.
- [ ] Q5 verified on required Python 3.9–3.11.
- [ ] Screenshots captured.
- [ ] PR reviewed and merged.
- [ ] Q4/Q5 report sections completed.
- [ ] Meaningful Git history exists.
- [ ] Can trace A* code.
- [ ] Can explain Q5 state design.
- [ ] Can explain Q1-Q7 at viva level.
