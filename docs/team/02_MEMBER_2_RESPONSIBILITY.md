# Member 2 — Responsibility & Task Plan

## Role

**Assigned Student:** Atheek Fareez  
**Git Branch:** `feature/q2-q3-atheek`  
**Role:** Cost-Based Search Developer  
**Primary Questions:** Q2 — BFS, Q3 — Uniform Cost Search  
**Primary File:** `search.py`

---

# 1. Primary Development Work

## Q2 — Breadth First Search

Implement:

```python
breadthFirstSearch(problem)
```

Requirements:

- graph-search version;
- use `util.Queue`;
- track expanded states;
- return the required action path.

### Test

```bash
python autograder.py -q q2
```

## Q3 — Uniform Cost Search

Implement:

```python
uniformCostSearch(problem)
```

Requirements:

- use `util.PriorityQueue`;
- prioritize accumulated path cost;
- use actual cost rather than simply the number of actions.

### Test

```bash
python autograder.py -q q3
```

---

# 2. Technical Knowledge Ownership

Member 2 should have the deepest understanding of:

```text
BFS -> Queue -> FIFO
UCS -> PriorityQueue -> g(n)
```

Be able to explain:

- FIFO;
- accumulated cost;
- priority queue ordering;
- BFS versus UCS;
- unit-cost versus varying-cost behavior;
- optimality of UCS.

---

# 3. Secondary Responsibilities

Review:

- Member 1 Q1;
- Member 3 Q4 A*;
- Member 4 Q7 food heuristic.

During review, focus on correctness and how the algorithms interact with the shared search skeleton.

---

# 4. Testing Responsibilities

Primary:

```bash
python autograder.py -q q2
python autograder.py -q q3
```

Integration:

```bash
python autograder.py -q q1
python autograder.py -q q4
python autograder.py -q q7
python autograder.py
```

Record all final results and screenshots.

---

# 5. Git Responsibilities

Branch:

```text
feature/q2-q3-member2
```

Recommended commits:

```text
feat(search): implement BFS using util.Queue
feat(search): implement UCS with accumulated path cost
test(q2-q3): verify BFS and UCS
fix(q3): correct priority cost handling
docs(report): add q2-q3 evidence
```

---

# 6. Report Responsibilities

Write:

- Q2 section;
- Q3 section;
- Q2/Q3 autograder screenshots;
- concise algorithm/data-structure explanation.

Keep each question within 200 words.

---

# 7. Viva Preparation

Be able to answer:

- Why Queue for BFS?
- Why PriorityQueue for UCS?
- What is `g(n)`?
- Why isn't UCS identical to BFS?
- Can UCS choose a longer action sequence?
- Why does actual accumulated cost matter?
- How does graph search prevent repeated expansion?

Also learn Q1, Q4, Q5, Q6 and Q7 well enough to defend the complete project.

---

# 8. Definition of Done

- [ ] Q2 implemented.
- [ ] Q3 implemented.
- [ ] Q2 passes.
- [ ] Q3 passes.
- [ ] Screenshots captured.
- [ ] Peer reviews completed.
- [ ] PR merged.
- [ ] Q2/Q3 report sections completed.
- [ ] Meaningful Git history exists.
- [ ] Can defend BFS/UCS.
- [ ] Can explain Q1-Q7 overall.
