import time


def dfs(adj_list, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            for neighbour in adj_list[current_node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    time.sleep(0.1)

    return visited
