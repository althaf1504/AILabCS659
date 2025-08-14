from collections import deque

def is_valid(state):
    jug1, jug2, jug3 = state
    return 0 <= jug1 <= 8 and 0 <= jug2 <= 5 and 0 <= jug3 <= 3

def get_successors(state):
    jug1, jug2, jug3 = state
    capacities = (8, 5, 3)
    successors = []
    
    # Try pouring from one jug to another
    for i in range(3):
        for j in range(3):
            if i != j:
                amounts = [jug1, jug2, jug3]
                # Pour from jug i to jug j
                pour_amount = min(amounts[i], capacities[j] - amounts[j])
                amounts[i] -= pour_amount
                amounts[j] += pour_amount
                new_state = tuple(amounts)
                if is_valid(new_state):
                    successors.append(new_state)
    return successors

def bfs(start_state, goal_state):
    queue = deque([(start_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state == goal_state:
            return path
        for successor in get_successors(state):
            queue.append((successor, path))
    return None

start_state = (8, 0, 0)
goal_state = (4, 4, 0)

solution = bfs(start_state, goal_state)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
