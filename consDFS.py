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
