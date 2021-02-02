def dfs(visited, node, graph, path, dest):
    if node not in visited:
        visited.add(node)
        path.append(node)
        if node == dest:
            print(path)
            visited = set()
            return path
        else:
            for neighbor in graph[node]:
                dfs(visited, neighbor, graph, path, dest)

##visited = set()
##path = []
##dest = 'F'

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

s = 'A'
d = 'F'
V = 5
visited = set()
path = []

all_paths = []
def get_all_paths(u, d, visited, path): 
    visited.add(u)
    path.append(u)

    if u == d:
        all_paths.append(path.copy())
        
    else:
        for i in graph[u]:
            if i not in visited:
                get_all_paths(i, d, visited, path)
                
    path.pop()
    visited.discard(u)

get_all_paths(s,d, visited, path)
