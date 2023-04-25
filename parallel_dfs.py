import time
import multiprocessing


def sequential_dfs(adj_list, start_node, visited):
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            for neighbour in adj_list[current_node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    time.sleep(0.1)

    return visited


def init_pool(adj_list, num_processes, visited):
    global ADJ_LIST, NUM_PROCESSES, VISITED
    ADJ_LIST = adj_list
    NUM_PROCESSES = num_processes
    VISITED = visited


def parallel_dfs(adj_list, start_node, num_processes):
    visited = multiprocessing.Array('i', len(adj_list), lock=False)

    with multiprocessing.Pool(initializer=init_pool,
                              initargs=(adj_list, num_processes, visited)) as pool:
        results = []
        for i in range(num_processes):
            result = pool.apply_async(sequential_dfs, args=(adj_list, i))
            results.append(result)
        for result in results:
            result.wait()

    return visited
