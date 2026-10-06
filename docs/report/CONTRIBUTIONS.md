# Individual Team Contributions

| Member Name | Student ID | Primary Responsibilities | Git Branch | Report Section |
|---|---|---|---|---|
| Member 1 | - | Q1 (DFS) | `feature/q1-dfs-member1` | Section 2.1 |
| Member 2 | - | Q2 (BFS) & Q3 (UCS) | `feature/q2-q3-atheek` | Section 2.2 & 2.3 |
| Member 3 | - | Q4 (A*) & Q5 (Corners Problem) | `feature/q4-q5-member3` | Section 3.1 & 3.2 |
| Member 4 | - | Q6 (Corners Heuristic) & Q7 (Food Heuristic) | `feature/q6-q7-member4` (planned) | Section 3.3 & 3.4 |

This table records the agreed responsibility allocation, not proof of original
code authorship. It supersedes the older allocation that assigned Q4 to Member
4, Q5 to Member 1, and Q3/Q7 to Member 3. Coordinate the older Member 1 branch's
Q5 report/evidence attribution before merging report changes.

Member 3's actual work on 2026-10-07: fix SearchAgent's selected-heuristic
forwarding; add seven regression tests; verify the existing Q4/Q5 implementations
against the downloaded Berkeley tests; document the Q5 state contract; and
reproduce the Q6 issue for Member 4. Existing A*/CornersProblem code predates
this branch and was not rewritten. Finalization on 2026-10-07 passed official
Berkeley Q4/Q5, custom Q4/Q5, and seven regression tests on Python 3.11.9.
See [verification evidence](../testing/MEMBER3_VERIFICATION.md).
