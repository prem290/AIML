from collections import deque

# Graph
graph = {
    'Alice': ['Charlie', 'David'],
    'Charlie': ['Alice', 'Emma'],
    'David': ['Alice', 'Emma', 'Fred'],
    'Emma': ['Charlie', 'David', 'Bob'],
    'Fred': ['David', 'Bob'],
    'Bob': ['Emma', 'Fred']
}

# BFS
def bfs(start, goal):
    queue = deque([[start]])
    visited = []

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.append(node)

            if node == goal:
                return path

            for neighbor in graph[node]:
                queue.append(path + [neighbor])

# DFS
def dfs(start, goal):
    stack = [[start]]
    visited = []

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.append(node)

            if node == goal:
                return path

            for neighbor in reversed(graph[node]):
                stack.append(path + [neighbor])

# Main
print("BFS Path:", " -> ".join(bfs("Alice", "Bob")))
print("DFS Path:", " -> ".join(dfs("Alice", "Bob")))