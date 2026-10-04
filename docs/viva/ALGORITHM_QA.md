# Viva Q&A Cheat Sheet

### Q: Why is BFS optimal for unweighted graphs, but not for graphs with arbitrary costs?
**A:** BFS expands nodes in order of path depth. When step costs are all equal (1), path depth equals total path cost. If edge costs vary, a deeper node might have lower total cost, requiring UCS.

### Q: What happens if a heuristic is admissible but inconsistent?
**A:** A* search with graph search (using a visited set) might explore a node via a sub-optimal path first and discard later optimal paths to that node, leading to sub-optimal solutions unless re-opening of nodes is allowed.
