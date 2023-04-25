

# def dfs(adj_list, start, target):
#     visited = set()
#     stack = [(start, [])]
#     print(stack)
#     while stack:
#         node, path = stack.pop()
#         print(node)
#         print(path)
#         if node not in visited:
#             if node == target:
#                 print(path + [node])
#                 return path + [node]
#             visited.add(node)
#             print(visited)
#             for neighbour in adj_list[node]:
#                 print(adj_list[node])
#                 print(neighbour)
#                 stack.append((neighbour, path + [str(node)]))
#                 print(stack)
#     return 'Target not found in graph'

# def dfs(adj_list, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#
#     print(start)
#
#     for neighbour in adj_list[start] - visited:
#         dfs(adj_list, neighbour, visited)
#
#     print(visited)
#     return visited

# DFS PSEUDOCODE
# DFS(G, v):
#     visited = set()
#     stack = [v]
#
#     while stack is not empty:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#
#             for neighbour in G[node]:
#                 if neighbour not in visited:
#                     stack.append(neighbour)
#
#     return visited

def dfs(adj_list, start_node):
    visited = set()
    visited_order = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited_order:
            visited.add(current_node)
            visited_order.append(current_node)
            for neighbour in adj_list[current_node]:
                if neighbour not in visited_order:
                    stack.append(neighbour)

    return visited, visited_order

# def dfs(graph, start):
#     visited = set()
#     stack = [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#     return visited

# def dfs(adj_list, start):
#     visited = []
#     stack = [start]
#
#     while stack:
#         current_node = stack.pop()
#         if current_node not in visited:
#             visited.append(current_node)
#             for neighbour in adj_list[current_node]:
#                 if neighbour not in visited:
#                     stack.append(neighbour)
#
#     return visited




