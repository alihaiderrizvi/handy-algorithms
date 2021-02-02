def is_cyclic(numNodes, connections):
    graph = {}
    indegree = {}

    for i in range(numNodes):
        graph[i] = []
        indegree[i] = 0

    for i,j in connections:
        graph[i].append(j)
        indegree[j] += 1

    queue = []

    for i in indegree:
        if indegree[i] == 0:
            queue.append(i)

    count = 0

    while queue:
        curr = queue.pop(0)
        count += 1

        for node in graph[curr]:
            indegree[node] -= 1
            if indegree[node] == 0:
                queue.append(node)

    return count == numNodes
