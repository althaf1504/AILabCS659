from collections import deque
import random

# Course : CS307 Artificial Intelligence
# Exercise : Puzzle Eight Solver
# Learning Objective : Revisit concepts of basic data structures, BFS and DFS

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def get_successors(node):
    successors = []
    index = node.state.index(0)  # position of empty tile (0)
    quotient = index // 3
    remainder = index % 3
    moves = []

    # Row constrained moves
    if quotient == 0:
        moves = [3]             # can only move down
    elif quotient == 1:
        moves = [-3, 3]         # can move up and down
    elif quotient == 2:
        moves = [-3]            # can only move up

    # Column constrained moves
    if remainder == 0:
        moves += [1]            # can move right
    elif remainder == 1:
        moves += [-1, 1]        # can move left and right
    elif remainder == 2:
        moves += [-1]           # can move left

    for move in moves:
        im = index + move
        if 0 <= im < 9:  # within bounds
            new_state = list(node.state)
            new_state[index], new_state[im] = new_state[im], new_state[index]  # swap
            successor = Node(new_state, node)
            successors.append(successor)            
    return successors

def bfs(start_state, goal_state):
    start_node = Node(start_state)
    goal_node = Node(goal_state)
    queue = deque([start_node])
    visited = set()
    nodes_explored = 0

    while queue:
        node = queue.popleft()
        if tuple(node.state) in visited:
            continue
        visited.add(tuple(node.state))
        nodes_explored += 1

        if node.state == list(goal_node.state):
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            print('✅ Total nodes explored:', nodes_explored)
            return path[::-1]

        for successor in get_successors(node):
            queue.append(successor)

    print('❌ No solution found. Nodes explored:', nodes_explored)
    return None


# ---- Run Example ----
start_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # initial state
s_node = Node(start_state)

# Generate a random reachable goal state
D = 20
d = 0
while d <= D:
    goal_state = random.choice(get_successors(s_node)).state
    s_node = Node(goal_state)
    d += 1

print("🎯 Goal State:", goal_state)

solution = bfs(start_state, goal_state)
if solution:
    print("✅ Solution found! Path:")
    for step in solution:
        print(step)
else:
    print("❌ No solution found.")
