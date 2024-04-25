def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            print(v, end=' ')
            visited.add(v)
            stack.extend(graph.get(v, []))

# Example usage:
graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
dfs(graph, 1)
