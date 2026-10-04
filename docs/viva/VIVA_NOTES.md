# Individual Viva Defense Notes

## Key Concepts to Defend
1. **Graph Search vs Tree Search:** Why visited sets prevent infinite loops in cyclic mazes.
2. **Priority Queue Key Invariants:** How UCS priorities ($g(n)$) differ from A* priorities ($f(n) = g(n) + h(n)$).
3. **Corner Representation:** State as `( (x, y), (visited_c1, visited_c2, visited_c3, visited_c4) )`.
4. **Admissibility Proof:** Demonstrating $h(n) \le h^*(n)$ for Manhattan distance bounds.
