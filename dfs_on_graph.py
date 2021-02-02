def dfs(visited, node, graph):
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, neighbor, graph)

visited = set()

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

dfs(visited, 'A', graph)
print(visited)
