graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []

def dfs(graph,visited,node):
    if(node not in visited):
        print(node)
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph,visited,neighbor)

dfs(graph,visited,'A')