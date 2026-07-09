from collections import deque

# Social Network Graph
graph = {
    'Alice': ['Charlie', 'David'],
    'Bob': ['Emma', 'Fred'],
    'Charlie': ['Alice', 'Emma'],
    'David': ['Alice', 'Emma', 'Fred'],
    'Emma': ['Bob', 'Charlie', 'David'],
    'Fred': ['Bob', 'David']
}

# Arrange neighbors alphabetically
for node in graph:
    graph[node].sort()


# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    print("\n===== BFS Traversal =====")

    while queue:
        print("Queue:", list(queue))
        current = queue.popleft()

        print("Visited:", visited)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nBFS Path:")
    print(" -> ".join(path))


# ---------------- DFS ----------------
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    print("\n===== DFS Traversal =====")

    while stack:
        print("Stack:", stack)

        current = stack.pop()

        if current not in visited:
            visited.add(current)

            print("Visited:", visited)

            if current == goal:
                break

            # Reverse alphabetical push
            for neighbor in sorted(graph[current], reverse=True):
                if neighbor not in visited:
                    if neighbor not in parent:
                        parent[neighbor] = current
                    stack.append(neighbor)

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nDFS Path:")
    print(" -> ".join(path))


# Driver Code
start = "Alice"
goal = "Bob"

bfs(graph, start, goal)
dfs(graph, start, goal)