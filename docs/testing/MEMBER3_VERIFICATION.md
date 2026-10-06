# Member 3 verification — 2026-10-07

## Scope and provenance

Starting commit: `43e6cdeb5f2b2efde3510cf6e8fe4b221b14ec12`.
Tested branch HEAD for finalization: `b029a05` (production code unchanged since
`81faccf`, `fix(search-agent): forward selected heuristic to A*`).
Branch: `feature/q4-q5-member3`, created from clean `main` after fetching origin
and confirming that this branch did not exist remotely.

Existing `aStarSearch` and the entire `CornersProblem` class were preserved.
The only production-code change binds the selected heuristic in `SearchAgent`
when the selected function supports it, following the official starter's
dispatch pattern. No DFS/BFS/UCS or Q6/Q7 heuristic implementation was edited.

These are actual execution results, not claims of original Q4/Q5 authorship.

## Supported-runtime verification — 2026-10-07

Finalization tests ran on **CPython 3.11.9** from the project's `.venv`:
`C:\Users\WAZNI\Desktop\SLIIT\PROJECTS\Y3\Y3-S1\IA\Pac-Man Intelligent Search\.venv\Scripts\python.exe`.
This meets the required Python 3.9–3.11 range. The existing environment was
activated for repository tests; the same executable was used explicitly for
official tests. No Python installation or dependency changes were made.

The earlier execution phase used Python 3.14.3. Its results remain historical
evidence; the supported-runtime results below supersede the runtime limitation.
Bare `python` in an unactivated shell still resolves to Python 3.14.3, so activate
`.venv` or call its executable directly. Verification date: **2026-10-07,
Asia/Colombo**.

## Official Berkeley infrastructure

Downloaded the exact [search.zip linked in the assignment](https://inst.eecs.berkeley.edu/~cs188/sp26/assets/projects/search.zip).
Archive version: `v1.004`.

Archive SHA256:
`d212f664b97ee38548dd868dfc5ce187f1a2147cfb90b0469e4fffe6e0a160c3`

Temporary location, outside this Git repository:
`../temp/member3-verification-20261007/`.

- `official/search/`: untouched archive extraction.
- `submission/`: separate copy of the official project, with only its
  `search.py` and `searchAgents.py` replaced by exact copies of this repository's
  two `src/` files.
- `official-q4-after.txt` and `official-q5-after.txt`: captured post-fix output.
- `official-q4-python311.txt` and `official-q5-python311.txt`: captured final
  Python 3.11.9 output, separate from the earlier Python 3.14.3 logs.
- `q6_diagnostic.py`: independent remaining-cost BFS and Q6 reproduction.

No adapter was necessary. Copying the two submission files into the official
flat directory was the only accommodation for the repository's `src/` layout.
The official engine, utilities, autograder, fixtures, and expected answers were
unchanged; a byte comparison of every non-submission official file confirmed
this after testing. No solution-generation option was used.

The archive contains `test_cases/q1` through `q8`, six Q4 tests, one Q5 test,
and 37 layouts including `trickySearch`. The repository's root autograder
remains a separate custom smoke suite with no official `test_cases/` tree.

## OFFICIAL Berkeley results — Python 3.11.9

From the temporary `submission/` directory, using the project virtual
environment's executable (the relative path resolves outside the temporary
environment to the repository):

```powershell
& '..\..\..\Pac-Man Intelligent Search\.venv\Scripts\python.exe' -B autograder.py -q q4 --no-graphics
& '..\..\..\Pac-Man Intelligent Search\.venv\Scripts\python.exe' -B autograder.py -q q5 --no-graphics
```

Both commands passed during finalization on Python 3.11.9. They also passed
before and after the SearchAgent fix in the earlier Python 3.14.3 execution.
The two temporary submission files were refreshed from the current repository
and verified byte-for-byte. All official non-submission files were compared
against the untouched extraction again and remained identical.

| Test | Result | Evidence |
|---|---|---|
| Q4 `astar_0.test` | PASS | `Right, Down, Down` |
| Q4 `astar_1_graph_heuristic.test` | PASS | `0, 0, 2` |
| Q4 `astar_2_manhattan.test` | PASS | Official mediumMaze: cost 68, expanded 221 |
| Q4 `astar_3_goalAtDequeue.test` | PASS | Cheaper goal path accepted on dequeue |
| Q4 `graph_backtrack.test` | PASS | Official expected path/expansion checks |
| Q4 `graph_manypaths.test` | PASS | Official expected path/expansion checks |
| Q5 `corner_tiny_corner.test` | PASS | Official tinyCorner: optimal length 28 |

Berkeley scores: **Q4 3/3, Q5 3/3**. Q5 automatically runs its Q2 dependency;
all five Q2 tests also passed, scoring 3/3. These Berkeley raw points are not
the assignment's 4-mark Q4 / 8-mark Q5 allocation; no conversion is asserted.
These results do not establish that the entire submission passes Q1–Q7.

## CUSTOM repository results — Python 3.11.9

From the repository root:

```powershell
. .\.venv\Scripts\Activate.ps1
python --version # Python 3.11.9
python -B autograder.py -q q4
python -B autograder.py -q q5
python -B -m unittest discover -s tests -v
```

All three test commands above passed during finalization on Python 3.11.9.

| Check | Result |
|---|---|
| Custom Q4 | 3/3; local mediumMaze cost 20, expanded 20 |
| Custom Q5 | 3/3; local tinyCorners cost 11 / expanded 114; mediumCorners cost 42 / expanded 684 |
| Member 3 unittest suite | 7/7 tests passed |

Historical integration evidence: `python -B autograder.py` passed 22/22 on
Python 3.14.3 in the earlier execution phase. It was not rerun as a full suite
during this finalization; the supported-runtime checks target Member 3's scope.

Before the fix, the selected-Manhattan test failed for both `astar` and
`aStarSearch`: the heuristic call count was zero. After the fix, both invoke
the selected heuristic with a state and problem. Other tests verify BFS/DFS/UCS
selection without heuristic invocation, default A*/UCS path agreement, all
four starting corners, hashability, all 16 goal-flag combinations, independent
successor flags, corner revisits, walls, unit costs, `_expanded`, and action costs.

## Member 4 coordination — Q6 defect remains

This is a **custom diagnostic on the repository's local tinyCorners**, not an
official Q6 grade. No Q6 implementation was modified.

Reachable state: `((3, 1), (False, False, False, True))`.
Reach it from the local layout's initial state using:
`East, East, East, West, West, South, South, South`.

- `cornersHeuristic` returns **12**.
- An independent bitmask BFS using only positions and walls finds true remaining
  optimal cost **9**.
- Optimal remaining actions:
  `East, East, West, West, West, West, North, North, North`.
- Legal consistency-violating transition:
  `((3,2), (False,False,False,True)) --North/1--> ((3,3), (False,False,False,True))`.
  Values are **13** and **10**, so **13 > 1 + 10**.

Q5 supplies the correct state and successors. The greedy heuristic calculation
is responsible for these violations. The custom Q6 smoke test nevertheless
reports 3/3 (cost 42, expanded 50), demonstrating its coverage limitation.

## Compatibility findings and outstanding work

- Q4/Q5 interfaces and PriorityQueue calls work with the official framework.
- The official SearchAgent binds heuristics; the repository previously did not.
- Official SearchAgent uses `searchType`; this repository uses `problemType`.
  No public signature was changed by the focused fix.
- Official helper definitions missing from this repository's `searchAgents.py`:
  `AStarCornersAgent`, `AStarFoodSearchAgent`, `StayEastSearchAgent`,
  `StayWestSearchAgent`, and `mazeDistance`. Q4/Q5 tests do not require them,
  but broader official integration needs team review. They were not added here.
- Local and official mazes differ; their costs/expansion counts are not comparable.
- Supported Python 3.11.9 Q4/Q5 and regression verification is complete.
  Lecturer-specific score mapping, screenshots, team review, exact AI prompt
  recording, and Q6 correction remain pending. No main merge is part of this work.

## AI usage record review

`docs/report/AI_USAGE.md` previously recorded only documentation scaffolding.
Member 3 used Codex for diagnosis, the SearchAgent integration fix, regression
tests, verification, and documentation/finalization. Existing entries were
preserved and this scope was recorded accurately. No exact Member 3 diagnosis
or execution prompt record was found in the project files inspected; preserving
the original prompts in the report record remains pending. No historical prompt
was reconstructed or invented, and no screenshots were generated or claimed.
