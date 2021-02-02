def bfs_on_graph(graph, root, visited):
    queue = []
    visited.append(root)
    queue.append(root)

    while queue:
        curr = queue.pop(0)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = []
bfs_on_graph(graph, 'A', visited)
