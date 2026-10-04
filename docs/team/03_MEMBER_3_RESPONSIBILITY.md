# Member 3 — Responsibility & Task Plan

## Role

**Role:** A* and Search-Problem Modeling Lead  
**Primary Questions:** Q4 — A* Search, Q5 — CornersProblem  
**Primary Files:** `search.py`, `searchAgents.py`

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

Conceptually, the state may be structured as:

```text
(PacmanPosition, VisitedCorners)
```

The exact representation must remain compatible with the provided starter code/autograder.

This allows Member 4 to design Q6 while Member 3 implements the concrete representation.

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
feat(search): implement A* using g+h priority
feat(corners): implement CornersProblem state
test(q4-q5): verify A* and CornersProblem
fix(corners): correct visited-corner bookkeeping
docs(report): add q4-q5 evidence
```

Avoid broad refactoring that creates merge conflicts for the rest of the team.

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

- [ ] Q4 implemented.
- [ ] Q5 implemented.
- [ ] Q5 state contract agreed with Member 4.
- [ ] Q4 passes.
- [ ] Q5 passes.
- [ ] Screenshots captured.
- [ ] PR reviewed and merged.
- [ ] Q4/Q5 report sections completed.
- [ ] Meaningful Git history exists.
- [ ] Can trace A* code.
- [ ] Can explain Q5 state design.
- [ ] Can explain Q1-Q7 at viva level.
