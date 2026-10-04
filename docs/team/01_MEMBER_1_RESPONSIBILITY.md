# Member 1 — Responsibility & Task Plan

## Role

**Role:** Search Algorithm Developer — DFS Lead  
**Primary Question:** Q1 — Depth First Search  
**Primary File:** `search.py`

---

# 1. Primary Development Work

## Q1 — Depth First Search

Implement:

```python
depthFirstSearch(problem)
```

The implementation must be the graph-search version and must track expanded states so the same state is not expanded repeatedly.

Use:

```text
util.Stack
```

The function must preserve the provided function signature and expected return format.

### Test

```bash
python autograder.py -q q1
```

---

# 2. Technical Knowledge Ownership

Member 1 should have the deepest understanding of:

- `SearchProblem`;
- state;
- successor;
- goal test;
- fringe;
- graph search;
- expanded states;
- DFS;
- LIFO behavior;
- cycle handling;
- action-path construction.

Core rule:

```text
DFS -> Stack -> LIFO
```

---

# 3. Secondary Responsibility

Review Member 2's BFS/UCS implementation.

Check:

- graph-search structure;
- fringe behavior;
- state-expansion logic;
- cost handling in UCS;
- function signatures;
- unintended edits.

Also participate in final Q6/Q7 integration review.

---

# 4. Testing Responsibilities

Primary:

```bash
python autograder.py -q q1
```

Integration testing:

```bash
python autograder.py -q q2
python autograder.py
```

Record:

- pass/fail;
- score;
- node count if displayed;
- date;
- screenshot filename.

---

# 5. Git Responsibilities

Branch:

```text
feature/q1-dfs-member1
```

Recommended meaningful commits:

```text
feat(search): implement graph-search DFS
test(q1): verify DFS autograder
fix(q1): correct expanded-state handling
docs(report): add q1 evidence
```

Never create fake commits only to increase Git activity.

---

# 6. Report Responsibilities

Write the Q1 report section.

Include:

- changed function;
- algorithm logic;
- `util.Stack` usage;
- graph-search behavior;
- autograder evidence;
- screenshot.

Maximum 200 words for the Q1 explanation.

---

# 7. Viva Preparation

Be able to answer immediately:

- Why is DFS using a Stack?
- What does LIFO mean here?
- Why track expanded states?
- What happens with a cycle?
- Is DFS generally optimal?
- How is DFS different from BFS?
- How is the common graph-search skeleton implemented in the code?

Also understand Q2-Q7 sufficiently to explain another member's implementation.

---

# 8. Definition of Done

- [ ] Q1 implemented.
- [ ] Q1 passes.
- [ ] Q1 screenshot captured.
- [ ] Peer review completed.
- [ ] PR merged.
- [ ] Q1 report section completed.
- [ ] Meaningful Git commits exist.
- [ ] Can explain Q1 line-by-line.
- [ ] Can explain Q1-Q7 at viva level.
