# IT3012 Intelligent Agents — Master To-Do List

## A. Team Setup
- [x] Confirm all 4 members.
- [x] Record names and student IDs.
- [x] Assign Member 1-4.
- [x] Create communication channel.
- [x] Agree branch naming.
- [x] Agree PR/review process.
- [x] Agree testing workflow.
- [x] Agree that everyone learns Q1-Q7.

## B. Environment
- [x] Install Python 3.9-3.11.
- [x] Create Virtual environment (`.venv`).
- [x] Activate environment.
- [x] Install required dependencies.
- [x] Run `python pacman.py`.
- [x] Verify Pac-Man is playable.
- [x] Record environment details in `docs/ENVIRONMENT.md`.

## C. Repository Setup
- [x] Create local / public GitHub repository structure.
- [x] Add starter project files.
- [x] Create `main` branch.
- [x] Create `.gitignore`.
- [x] Create `README.md`.
- [x] Create `docs/` folder structure (`project/`, `report/`, `team/`, `testing/`, `viva/`).
- [x] Add group plan (`00_GROUP_PARALLEL_PLAN.md`).
- [x] Add member responsibility files.
- [x] Add `TEST_RESULTS.md`.
- [x] Add `AI_USAGE.md`.
- [x] Add `REPORT_OUTLINE.md`.
- [x] Add `VIVA_NOTES.md`.

## D. Baseline Verification & Algorithmic Core
- [x] Inspect `search.py` interface.
- [x] Inspect `searchAgents.py` problem classes.
- [x] Read `util.py` data structures (`Stack`, `Queue`, `PriorityQueue`).
- [x] Read `autograder.py`.
- [x] Run autograder verification suite.

## E. Question 1 — Depth First Search (DFS)
- [x] Implement DFS in `src/search.py`.
- [x] Use `util.Stack`.
- [x] Track visited states to prevent infinite loops.
- [x] Preserve function signature.
- [x] Run Q1 autograder (PASSED).

## F. Question 2 & 3 — BFS + UCS
- [x] Implement BFS in `src/search.py` using `util.Queue` (PASSED).
- [x] Implement UCS in `src/search.py` using `util.PriorityQueue` with path cost (PASSED).

## G. Question 4 & 5 — A* Search + Corners Problem
- [x] Implement A* Search in `src/search.py` using `PriorityQueue` with $g(n) + h(n)$ (PASSED).
- [x] Implement `CornersProblem` in `src/searchAgents.py` with state $(pos, visitedCorners)$ (PASSED).

## H. Question 6 & 7 — Corners & Food Heuristics
- [x] Implement `cornersHeuristic` in `src/searchAgents.py` (Admissible & Consistent) (PASSED).
- [x] Implement `foodHeuristic` in `src/searchAgents.py` (Admissible & Consistent) (PASSED).

## I. User Interface & Interactive Enhancements
- [x] Modern Cyber Dark Neon Theme in `graphicsDisplay.py`.
- [x] Interactive Bottom Toolbar with Buttons: `BFS`, `DFS`, `UCS`, `A* Search`.
- [x] Added `🔄 Retry` button to reset maze back to starting state.
- [x] Added `🧪 Autograder` button to execute test suite directly from UI.
- [x] Non-closing persistent window after completing game/path.
- [x] GUI Error Pop-up dialog (`messagebox.showerror`) when an algorithm is disconnected or fails.

---

## PENDING / REMAINING TO-DO ITEMS

### J. Git Evidence & Screenshots
- [ ] Capture final autograder pass screenshots for Q1–Q7.
- [ ] Capture Git commit history and contribution graph screenshots.
- [ ] Verify public repository accessibility.

### K. Final Report Documentation
- [ ] Finalize section write-ups (<= 200 words per question explanation).
- [ ] Insert Q1–Q7 screenshots into `docs/report/REPORT_OUTLINE.md`.
- [ ] Add individual team member contribution table.
- [ ] Export final PDF report.

### L. AI Usage Documentation
- [ ] Review `docs/report/AI_USAGE.md` for completeness.
- [ ] Include AI declaration in final PDF report.

### M. Viva Preparation
- [ ] Review `docs/viva/VIVA_NOTES.md`.
- [ ] Practice 6-minute group viva walkthrough (explaining DFS, BFS, UCS, A*, Q5 state, Q6/Q7 heuristics).

### N. Final Submission Packaging
- [ ] Create submission ZIP containing `search.py` and `searchAgents.py`.
- [ ] Verify ZIP contents contain ONLY `search.py` and `searchAgents.py`.
- [ ] Submit PDF Report + Submission ZIP on LMS.
