# Member 4 — Responsibility & Task Plan

## Role

**Assigned Student:** Raashidh Rizvi  
**Student ID:** IT24104191  
**Git Branch:** `feat(heuristic)--implement-admissible-corners-heuristic-for-Q6`  
**Role:** Heuristic and Performance Lead  
**Primary Questions:** Q6 — Corners Heuristic, Q7 — Food Heuristic  
**Primary File:** `searchAgents.py`

---

# 1. Primary Development Work

## Q6 — Corners Heuristic

Implement:

```python
cornersHeuristic(state, problem)
```

Requirements:

- admissible;
- consistent;
- non-negative;
- zero at any goal state;
- preserve optimality;
- reduce unnecessary node expansion.

### Test

```bash
python autograder.py -q q6
```

The assignment grades node expansion on `mediumCorners` using these thresholds:

| Nodes Expanded | Marks |
|---:|---:|
| > 2000 | 0/8 |
| <= 2000 | 4/8 |
| <= 1600 | 6/8 |
| <= 1200 | 8/8 |

If the heuristic is inadmissible, or A* returns a non-optimal path on a required test, Q6 receives zero regardless of node count.

## Q7 — Food Heuristic

Implement:

```python
foodHeuristic(state, problem)
```

Requirements:

- admissible;
- consistent;
- efficient enough for the grading threshold.

### Test

```bash
python autograder.py -q q7
```

The assignment grades node expansion on `trickySearch` using:

| Nodes Expanded | Marks |
|---:|---:|
| > 15000 | 2/8 |
| <= 15000 | 4/8 |
| <= 12000 | 6/8 |
| <= 9000 | 8/8 |

---

# 2. Development Order

Use this order:

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

Do not optimize the heuristic first and only later attempt to prove it valid.

---

# 3. Q6 Coordination With Member 3

Q6 depends on Q5's state representation.

Coordinate with Member 3:

```text
Member 3 -> defines/implements Q5 state
Member 4 -> designs Q6 based on that state
```

Agree early on:

- state structure;
- visited-corner representation;
- goal condition;
- how remaining corners are identified.

This permits parallel design and implementation.

---

# 4. Q7 Technical Ownership

Member 4 should deeply understand:

- `FoodSearchProblem`;
- search state;
- remaining food;
- lower-bound heuristics;
- admissibility;
- consistency;
- A* heuristic behavior;
- node expansion;
- performance trade-offs.

---

# 5. Secondary Responsibilities

Review:

- Member 3 Q5;
- Member 2 Q3/UCS;
- integration between A* and the heuristics.

Pay special attention to whether heuristic changes preserve optimality.

---

# 6. Testing Responsibilities

Primary:

```bash
python autograder.py -q q6
python autograder.py -q q7
```

After heuristic changes:

```bash
python autograder.py -q q5
python autograder.py -q q6
python autograder.py -q q7
python autograder.py
```

For each run record:

- score;
- node count;
- test configuration;
- screenshot;
- date.

---

# 7. Git Responsibilities

Branch:

```text
feature/q6-q7-member4
```

Recommended commits:

```text
feat(heuristic): implement corners heuristic
test(q6): benchmark mediumCorners node expansion
fix(q6): preserve heuristic admissibility
feat(heuristic): implement food heuristic
test(q7): benchmark trickySearch
perf(heuristic): reduce food-search expansions
docs(report): add q6-q7 evidence
```

Every performance improvement must remain defensible in terms of admissibility and consistency.

---

# 8. Report Responsibilities

Write:

- Q6 section;
- Q7 section;
- node-expansion evidence;
- screenshots.

Explain:

- what the heuristic estimates;
- why it is a lower bound;
- why it is admissible;
- why it is consistent;
- how it affects expansion count.

Maximum 200 words per question.

---

# 9. Viva Preparation

Be able to defend:

- admissibility;
- consistency;
- lower bounds;
- why overestimation is dangerous;
- why a stronger heuristic can reduce expansions;
- Q6 threshold;
- Q7 threshold;
- why the chosen heuristic remains optimal.

Also be able to explain DFS/BFS/UCS/A* and Q5 because the viva is for the entire project.

---

# 10. Definition of Done

- [ ] Q6 implemented.
- [ ] Q6 admissibility reason documented.
- [ ] Q6 consistency reason documented.
- [ ] Q6 optimality checked.
- [ ] Q6 node expansion recorded.
- [ ] Q7 implemented.
- [ ] Q7 admissibility reason documented.
- [ ] Q7 consistency reason documented.
- [ ] Q7 node expansion recorded.
- [ ] Regression tests passed.
- [ ] Screenshots captured.
- [ ] PR reviewed and merged.
- [ ] Q6/Q7 report sections completed.
- [ ] Can defend both heuristics mathematically.
- [ ] Can explain Q1-Q7 at viva level.
