# Code Walkthrough Reference

## General Search Pattern (`search.py`)
```python
def genericGraphSearch(problem, fringe, priority_fn=None):
    # 1. Initialize fringe with (start_state, actions_list, path_cost)
    # 2. Maintain visited dict/set
    # 3. Loop until fringe is empty:
    #    a. Pop state
    #    b. If goal state, return actions
    #    c. If state not visited (or lower cost path), expand successors
```
