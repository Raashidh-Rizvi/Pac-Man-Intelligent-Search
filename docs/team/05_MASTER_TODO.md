# IT3012 Intelligent Agents — Master To-Do List

## A. Team Setup

- [ ] Confirm all 4 members.
- [ ] Record names and student IDs.
- [ ] Assign Member 1-4.
- [ ] Create communication channel.
- [ ] Agree branch naming.
- [ ] Agree PR/review process.
- [ ] Agree testing workflow.
- [ ] Agree that everyone learns Q1-Q7.

## B. Environment

For every member:

- [ ] Install Python 3.9-3.11.
- [ ] Create Conda environment.
- [ ] Activate environment.
- [ ] Install NumPy.
- [ ] Install Matplotlib.
- [ ] Run `python pacman.py`.
- [ ] Verify Pac-Man is playable.
- [ ] Record environment details.

## C. Repository Setup

- [ ] Create public GitHub repository.
- [ ] Add all four members.
- [ ] Add starter project.
- [ ] Create `main` branch.
- [ ] Create `.gitignore`.
- [ ] Create `README.md`.
- [ ] Create `docs/` folder.
- [ ] Add group plan.
- [ ] Add member responsibility files.
- [ ] Add `TEST_RESULTS.md`.
- [ ] Add `AI_USAGE.md`.
- [ ] Add `REPORT_OUTLINE.md`.
- [ ] Add `VIVA_NOTES.md`.

## D. Baseline Verification

- [ ] Inspect `search.py`.
- [ ] Inspect `searchAgents.py`.
- [ ] Read `util.py`.
- [ ] Read `autograder.py`.
- [ ] Run Q1 baseline.
- [ ] Run Q2 baseline.
- [ ] Run Q3 baseline.
- [ ] Run Q4 baseline.
- [ ] Run Q5 baseline.
- [ ] Run Q6 baseline.
- [ ] Run Q7 baseline.
- [ ] Record baseline output.

## E. Member 1 — Q1 DFS

- [ ] Implement DFS.
- [ ] Use `util.Stack`.
- [ ] Track expanded states.
- [ ] Preserve function signature.
- [ ] Run Q1 autograder.
- [ ] Capture Q1 screenshot.
- [ ] Peer review.
- [ ] Open PR.
- [ ] Merge PR.
- [ ] Write Q1 report section.

## F. Member 2 — Q2 BFS + Q3 UCS

- [ ] Implement BFS.
- [ ] Use `util.Queue`.
- [ ] Run Q2.
- [ ] Capture Q2 screenshot.
- [ ] Implement UCS.
- [ ] Use `util.PriorityQueue`.
- [ ] Use accumulated path cost.
- [ ] Run Q3.
- [ ] Capture Q3 screenshot.
- [ ] Peer review.
- [ ] Open PR.
- [ ] Merge PR.
- [ ] Write Q2/Q3 report sections.

## G. Member 3 — Q4 A* + Q5 Corners

- [ ] Implement A*.
- [ ] Use `g(n)+h(n)` priority.
- [ ] Run Q4.
- [ ] Capture Q4 screenshot.
- [ ] Agree Q5 state contract with Member 4.
- [ ] Implement `getStartState`.
- [ ] Implement `isGoalState`.
- [ ] Implement `getSuccessors`.
- [ ] Implement successor bookkeeping.
- [ ] Keep state compact and hashable.
- [ ] Do not store wall grid in the state.
- [ ] Do not store the whole GameState in the state.
- [ ] Run Q5.
- [ ] Capture Q5 screenshot.
- [ ] Peer review.
- [ ] Open PR.
- [ ] Merge PR.
- [ ] Write Q4/Q5 report sections.

## H. Member 4 — Q6 + Q7 Heuristics

- [ ] Understand Q5 state contract.
- [ ] Design Q6 heuristic.
- [ ] Prove/justify admissibility.
- [ ] Prove/justify consistency.
- [ ] Check non-negativity.
- [ ] Check goal state returns zero.
- [ ] Verify optimality.
- [ ] Run Q6.
- [ ] Record `mediumCorners` node expansion.
- [ ] Optimize Q6 only after correctness.
- [ ] Design Q7 heuristic.
- [ ] Prove/justify admissibility.
- [ ] Prove/justify consistency.
- [ ] Run Q7.
- [ ] Record `trickySearch` node expansion.
- [ ] Optimize Q7 only after correctness.
- [ ] Capture screenshots.
- [ ] Peer review.
- [ ] Open PR.
- [ ] Merge PR.
- [ ] Write Q6/Q7 report sections.

## I. Integration

- [ ] Pull latest `main`.
- [ ] Merge all approved PRs.
- [ ] Resolve conflicts carefully.
- [ ] Do not overwrite another member's implementation.
- [ ] Run Q1.
- [ ] Run Q2.
- [ ] Run Q3.
- [ ] Run Q4.
- [ ] Run Q5.
- [ ] Run Q6.
- [ ] Run Q7.
- [ ] Run full autograder.
- [ ] Verify required names/signatures.
- [ ] Verify protected/reference files were not unintentionally changed.

## J. Git Evidence

- [ ] Each member has meaningful commits.
- [ ] Commit messages describe actual work.
- [ ] Contributions occur throughout the lifecycle.
- [ ] Each member has implementation contribution.
- [ ] Each member has review/support contribution.
- [ ] Capture commit-history screenshot.
- [ ] Capture contribution-graph screenshot.
- [ ] Capture PR/merge evidence.
- [ ] Verify repository is public.

## K. Report

- [ ] Cover page.
- [ ] Group member information.
- [ ] Setup information.
- [ ] Q1 explanation <= 200 words.
- [ ] Q1 autograder screenshot.
- [ ] Q2 explanation <= 200 words.
- [ ] Q2 screenshot.
- [ ] Q3 explanation <= 200 words.
- [ ] Q3 screenshot.
- [ ] Q4 explanation <= 200 words.
- [ ] Q4 screenshot.
- [ ] Q5 explanation <= 200 words.
- [ ] Q5 screenshot.
- [ ] Q6 explanation <= 200 words.
- [ ] Q6 screenshot.
- [ ] Q7 explanation <= 200 words.
- [ ] Q7 screenshot.
- [ ] Public Git repository URL.
- [ ] Git contribution evidence.
- [ ] Individual contribution table.
- [ ] AI usage declaration.
- [ ] Export PDF.
- [ ] Check PDF visually.

## L. AI Documentation

- [ ] Record AI tools actually used.
- [ ] Record exact prompts.
- [ ] Record whether AI was used for understanding, ideas, code, debugging, or writing.
- [ ] Validate AI suggestions against the assignment/autograder.
- [ ] Include the declaration in the report.

## M. Viva

Every member:

- [ ] Explain DFS.
- [ ] Explain BFS.
- [ ] Explain UCS.
- [ ] Explain A*.
- [ ] Explain Stack/Queue/PriorityQueue.
- [ ] Explain graph-search expansion.
- [ ] Explain Q5 state representation.
- [ ] Explain Q6 admissibility.
- [ ] Explain Q6 consistency.
- [ ] Explain Q7 admissibility.
- [ ] Explain Q7 consistency.
- [ ] Explain node expansion.
- [ ] Trace code line-by-line.
- [ ] Explain another member's question.
- [ ] Practice six-minute viva.

## N. Final Submission

- [ ] Final full autograder pass.
- [ ] Final Q1-Q7 screenshots.
- [ ] Final Git evidence.
- [ ] Final report PDF.
- [ ] Create code ZIP.
- [ ] ZIP contains ONLY `search.py` and `searchAgents.py`.
- [ ] Use correct Group ID in filenames.
- [ ] Open ZIP and verify contents.
- [ ] Open PDF and verify contents.
- [ ] Submit both items once per group.
