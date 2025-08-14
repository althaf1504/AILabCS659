from collections import deque

def is_valid(state):
    jug1, jug2, jug3 = state
    # Check jug capacity limits and non-negative amounts
    if jug1 > 8 or jug2 > 5 or jug3 > 3 or jug1 < 0 or jug2 < 0 or jug3 < 0:
        return False
    return True

def get_successors(state):
    successors = []
    jug1, jug2, jug3 = state
    capacities = (8, 5, 3)

    # All possible pour moves: (from_jug, to_jug)
    moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    for move in moves:
        amounts = [jug1, jug2, jug3]
        i, j = move
        pour_amount = min(amounts[i], capacities[j] - amounts[j])
        if pour_amount > 0:
            amounts[i] -= pour_amount
            amounts[j] += pour_amount
            new_state = tuple(amounts)
            if is_valid(new_state):
                successors.append(new_state)
    return successors

def check_goal_state(state):
    return state == goal_state

def bfs(start_state, goal_state):
    queue = deque([(start_state, [])])
    visited = set()
    while queue:
        (state, path) = queue.popleft()  # BFS uses popleft
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if check_goal_state(state):
            return path
        for successor in get_successors(state):
            queue.append((successor, path))
    return None

start_state = (8, 0, 0)
goal_state = (1, 4, 3)  # target state

solution = bfs(start_state, goal_state)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")

