# AIML Assignment 2 - Problem Solving Through Search
# Algorithms: BFS, DFS, UCS, Greedy Best-First, A*, Hill Climbing,
# Simulated Annealing, and 4-Queens CSP Backtracking.

from collections import deque
import heapq
import math
import random
import time
import pandas as pd

# Common graph and heuristic
graph = {"S": ["A", "B"], "A": ["B", "C"], "B": ["C", "G"], "C": ["G"], "G": []}
weighted_graph = {"S": [("A", 2), ("B", 5)], "A": [("B", 1), ("C", 6)], "B": [("C", 2), ("G", 8)], "C": [("G", 3)], "G": []}
heuristic = {"S": 7, "A": 5, "B": 4, "C": 2, "G": 0}
START, GOAL = "S", "G"

# BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])]); visited = {start}; expanded = 0
    while queue:
        node, path = queue.popleft(); expanded += 1
        if node == goal: return path, expanded
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor); queue.append((neighbor, path + [neighbor]))
    return None, expanded

# DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]; visited = set(); expanded = 0
    while stack:
        node, path = stack.pop()
        if node in visited: continue
        visited.add(node); expanded += 1
        if node == goal: return path, expanded
        for neighbor in reversed(graph[node]):
            if neighbor not in visited: stack.append((neighbor, path + [neighbor]))
    return None, expanded

# Uniform Cost Search
def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [start])]; best_cost = {start: 0}; expanded = 0
    while pq:
        cost, node, path = heapq.heappop(pq)
        if cost != best_cost.get(node): continue
        expanded += 1
        if node == goal: return path, cost, expanded
        for neighbor, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
    return None, float("inf"), expanded

# Greedy Best-First Search
def greedy_best_first(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [start])]; visited = set(); expanded = 0
    while pq:
        _, node, path = heapq.heappop(pq)
        if node in visited: continue
        visited.add(node); expanded += 1
        if node == goal: return path, expanded
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None, expanded

# A* Search
def a_star(graph, start, goal, heuristic):
    pq = [(heuristic[start], 0, start, [start])]; best_g = {start: 0}; expanded = 0
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best_g.get(node): continue
        expanded += 1
        if node == goal: return path, g, expanded
        for neighbor, edge_cost in graph[node]:
            new_g = g + edge_cost
            if new_g < best_g.get(neighbor, float("inf")):
                best_g[neighbor] = new_g
                heapq.heappush(pq, (new_g + heuristic[neighbor], new_g, neighbor, path + [neighbor]))
    return None, float("inf"), expanded

# 8-Queens helpers and Hill Climbing
def conflicts(state):
    total = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                total += 1
    return total

def hill_climbing(n=8, seed=42):
    random.seed(seed); state = [random.randrange(n) for _ in range(n)]; evaluated = 0
    while True:
        current = conflicts(state); neighbors = []
        for col in range(n):
            for row in range(n):
                if row != state[col]:
                    next_state = state[:]; next_state[col] = row; neighbors.append(next_state)
        evaluated += len(neighbors); best_state = min(neighbors, key=conflicts)
        if conflicts(best_state) >= current: return state, current, evaluated
        state = best_state

# Simulated Annealing
def simulated_annealing(n=8, steps=10000, seed=42):
    random.seed(seed); state = [random.randrange(n) for _ in range(n)]; current = conflicts(state)
    best_state = state[:]; best_score = current
    for step in range(steps):
        col = random.randrange(n); row = random.randrange(n); next_state = state[:]; next_state[col] = row
        new_score = conflicts(next_state); temperature = max(10 * (0.995 ** step), 1e-9); delta = new_score - current
        if delta < 0 or random.random() < math.exp(-delta / temperature): state, current = next_state, new_score
        if current < best_score: best_state, best_score = state[:], current
        if best_score == 0: break
    return best_state, best_score, step + 1

# 4-Queens CSP Backtracking
def solve_4_queens():
    n = 4; assignment = [-1] * n; assignments_tested = 0
    def safe(row, col):
        for previous_col in range(col):
            previous_row = assignment[previous_col]
            if previous_row == row or abs(previous_row - row) == abs(previous_col - col): return False
        return True
    def backtrack(col):
        nonlocal assignments_tested
        if col == n: return True
        for row in range(n):
            assignments_tested += 1
            if safe(row, col):
                assignment[col] = row
                if backtrack(col + 1): return True
                assignment[col] = -1
        return False
    solved = backtrack(0)
    return assignment, assignments_tested, solved

if __name__ == "__main__":
    print("BFS:", bfs(graph, START, GOAL))
    print("DFS:", dfs(graph, START, GOAL))
    print("UCS:", uniform_cost_search(weighted_graph, START, GOAL))
    print("Greedy:", greedy_best_first(graph, START, GOAL, heuristic))
    print("A*:", a_star(weighted_graph, START, GOAL, heuristic))
    print("Hill Climbing:", hill_climbing())
    print("Simulated Annealing:", simulated_annealing())
    print("4-Queens CSP:", solve_4_queens())
