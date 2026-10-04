# Regression Testing Strategy

## Overview
To prevent regressions when introducing heuristics or changing general search primitives, every PR merged into `main` must run the regression suite.

## Verification Checklist Before Merge
- [ ] `python autograder.py` passes all previously completed questions with 100% score.
- [ ] No extra nodes expanded compared to baseline benchmark measurements.
- [ ] Code formatted cleanly without breaking function signatures.
