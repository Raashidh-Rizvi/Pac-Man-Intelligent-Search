# IT3012 Intelligent Agents — Group Parallel Development Plan

## Assignment

**Module:** IT3012 — Intelligent Agents  
**Project:** Pac-Man Intelligent Search  
**Group Size:** 4 members

The assignment contains seven coding questions:

- Q1 — Depth First Search
- Q2 — Breadth First Search
- Q3 — Uniform Cost Search
- Q4 — A* Search
- Q5 — Corners Problem representation
- Q6 — Corners heuristic
- Q7 — Food heuristic

The assignment also assesses:

- Group Autograder Score — 40 marks
- Group Report — 10 marks
- Individual Git Contribution — 10 marks
- Individual Viva — 40 marks

The brief explicitly requires everyone to understand the **entire solution**, not only their own section. Therefore, the team should use parallel ownership plus peer review and cross-team learning. 

---

# 1. Parallel Development Model

All four members should work simultaneously rather than waiting for one question to finish before starting another.

```text
                         MAIN
                           |
          +----------------+----------------+
          |                |                |
          v                v                v                v
        MEMBER 1         MEMBER 2         MEMBER 3         MEMBER 4
          |                |                |                |
         Q1             Q2 + Q3           Q4 + Q5           Q6 + Q7
         DFS            BFS + UCS           A* + Corners      Heuristics
          |                |                |                  |
          +----------------+----------------+------------------+
                           |
                           v
                    Integration + Review
                           |
                           v
                     Full Autograder
                           |
                    +------+------+
                    |             |
                    v             v
                  Report        Viva
```

# 2. Function Ownership

To minimize Git conflicts, agree on exact function ownership before coding.

## `search.py`

```text
depthFirstSearch()        -> Member 1
breadthFirstSearch()      -> Member 2
uniformCostSearch()       -> Member 2
aStarSearch()             -> Member 3
```

## `searchAgents.py`

```text
CornersProblem methods   -> Member 3
cornersHeuristic()       -> Member 4
foodHeuristic()          -> Member 4
```

Each member should avoid unnecessary edits to another member's section.

---

# 3. Member Responsibilities

| Member | Primary Work | Secondary Work | Main File(s) |
|---|---|---|---|
| Member 1 | Q1 DFS | Q2 review, search skeleton review | `search.py` |
| Member 2 | Q2 BFS + Q3 UCS | Q1 review, Q7 review | `search.py` |
| Member 3 | Q4 A* + Q5 CornersProblem | Q6 review | `search.py`, `searchAgents.py` |
| Member 4 | Q6 + Q7 heuristics | Q5 review | `searchAgents.py` |

Use the individual files in this folder for the detailed responsibility of each person.

---

# 4. Git Branches

Recommended branches:

```text
main

feature/q1-dfs-member1
feature/q2-q3-member2
feature/q4-q5-member3
feature/q6-q7-member4
```

Every member works on their own branch and opens a Pull Request when a logical unit is ready.

---

# 5. Review Rotation

Recommended review cycle:

```text
Member 1 -> Member 2
Member 2 -> Member 3
Member 3 -> Member 4
Member 4 -> Member 1
```

Reviewers check:

- correctness;
- assignment requirements;
- function signatures;
- data structure usage;
- edge cases;
- unintended file changes;
- test evidence.

---

# 6. Parallel Testing

Member 1:

```bash
python autograder.py -q q1
```

Member 2:

```bash
python autograder.py -q q2
python autograder.py -q q3
```

Member 3:

```bash
python autograder.py -q q4
python autograder.py -q q5
```

Member 4:

```bash
python autograder.py -q q6
python autograder.py -q q7
```

After all work is integrated:

```bash
python autograder.py
```

---

# 7. Managing Dependencies Without Stopping Parallel Work

The main dependency is:

```text
Q5 CornersProblem
        |
        v
Q6 Corners Heuristic
```

The solution is to agree on the **Q5 state contract** early.

Conceptually:

```text
state = (PacmanPosition, VisitedCorners)
```

The exact representation must remain compatible with the starter project and autograder.

Then:

```text
Member 3 -> implements Q5 state representation
Member 4 -> designs and reasons about Q6 using the agreed state contract
```

This allows Q6 planning and development to happen in parallel with Q5 implementation.

Q7 is based on the provided `FoodSearchProblem`, so it can be developed independently once its state interface is understood.

---

# 8. Parallel Documentation

Do not postpone report work until the end.

```text
Member 1 -> Q1 report section + screenshot
Member 2 -> Q2/Q3 report sections + screenshots
Member 3 -> Q4/Q5 report sections + screenshots
Member 4 -> Q6/Q7 report sections + screenshots
```

Shared documentation should be maintained continuously:

```text
docs/TEST_RESULTS.md
docs/AI_USAGE.md
docs/REPORT_OUTLINE.md
docs/VIVA_NOTES.md
```

---

# 9. Git Commit Strategy

Commits should be genuine and meaningful.

Good examples:

```text
feat(search): implement graph-search DFS
feat(search): implement BFS using util.Queue
feat(search): implement UCS with accumulated path cost
feat(search): implement A* using g+h priority
feat(corners): implement compact corner state representation
feat(heuristic): implement corners heuristic
test(q6): benchmark mediumCorners node expansion
feat(heuristic): implement food heuristic
test(q7): benchmark trickySearch
fix(q5): correct corner visit bookkeeping
docs(report): add q1 evidence
```

Avoid meaningless commit messages such as:

```text
update
changes
fix
final
done
```

The goal is not to manufacture commits; it is to create a visible history of genuine contribution throughout the assignment lifecycle.

---

# 10. Report Requirements

For every Q1-Q7, record:

1. Specific functions/code blocks changed.
2. Autograder screenshot.
3. Concise explanation of logic/data structures.
4. Heuristic design explanation for Q6/Q7.
5. Keep each question explanation within the stated 200-word maximum.

At the end of the report include:

- public Git repository URL;
- Git commit-history evidence;
- contribution graph evidence;
- individual contribution table;
- AI usage declaration and exact prompts if AI was used.

---

# 11. Viva Strategy

The viva is individual. Every member should be able to explain every question.

Core concepts:

```text
DFS  -> Stack -> LIFO
BFS  -> Queue -> FIFO
UCS  -> PriorityQueue -> g(n)
A*   -> PriorityQueue -> g(n) + h(n)
```

Every member must also understand:

- graph-search state expansion;
- CornersProblem state representation;
- admissibility;
- consistency;
- optimality;
- node-expansion performance;
- the implementation written by each other member.

---

# 12. Final Definition of Done

The project is complete only when:

- [ ] Q1-Q7 pass.
- [ ] Q6 heuristic is admissible and consistent.
- [ ] Q7 heuristic is admissible and consistent.
- [ ] Q6/Q7 performance results are recorded.
- [ ] Required functions/files/classes retain their names.
- [ ] No protected/reference file was unintentionally changed.
- [ ] All four members have meaningful Git contributions.
- [ ] All four members understand the complete codebase.
- [ ] Report screenshots are collected.
- [ ] Git evidence is collected.
- [ ] AI usage is documented accurately.
- [ ] Final PDF is checked.
- [ ] Final code ZIP contains only `search.py` and `searchAgents.py`.
