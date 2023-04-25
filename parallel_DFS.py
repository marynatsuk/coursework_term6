import multiprocessing

def cons_dfs(adj_list, start_node, visited):
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            for neighbour in adj_list[current_node]:
                if neighbour not in visited:
                    stack.append(neighbour)
    return visited


def init_pool(adj_list, num_processes, visited):
    global ADJ_LIST, NUM_PROCESSES, VISITED
    ADJ_LIST = adj_list
    NUM_PROCESSES = num_processes
    VISITED = visited


def divide_list(adj_list, num_parts):
    my_tree = [[neighbour for neighbour in adj_list[node]] for node in adj_list]
    quotient = len(adj_list) // num_parts
    remainder = len(adj_list) % num_parts
    sublists = []
    start = 0
    for i in range(num_parts):
        end = start + quotient + (i < remainder)
        sublists.append(my_tree[start:end])
        start = end
    #sublists = [my_tree[i::num_parts] for i in range(num_parts)]
    return sublists


def parallel_dfs(adj_list, start_node, num_processes):
    visited = multiprocessing.Array('i', len(adj_list), lock=False)
    sub_lists = divide_list(adj_list, num_processes)

    with multiprocessing.Pool(initializer=init_pool, initargs=(adj_list, num_processes, visited)) as pool:
        results = []
        for sub_adj_list in sub_lists:
            result = pool.apply_async(cons_dfs, args=(sub_adj_list, start_node))
            results.append(result)
        for result in results:
            result.wait()

    return visited
