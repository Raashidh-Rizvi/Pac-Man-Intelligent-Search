# Git Workflow Rules

1. **Never commit directly to `main` branch.**
2. All development takes place on assigned feature branches (`feature/q1-dfs`, `feature/q2-bfs`, etc.).
3. Commit messages must be clear and descriptive:
   `git commit -m "feat(q1): implement depth-first graph search with visited set"`
4. Pull requests must include passing autograder test results before merging.
