import pandas as pd
import time

import create_tree, sequential_dfs, parallel_dfs

excel_path = 'C:/Users/serg/PycharmProjects/tpo_coursework_final/results.xlsx'
balanced_json_path = 'C:/Users/serg/PycharmProjects/tpo_coursework_final/balanced_list_json/'

NUM_TESTS = 1
sequential_time = []
parallel_time = []
visited = []


def time_results(sequential_time_results, parallel_time_results):
    average_sequential = round(sum(sequential_time_results) / NUM_TESTS, 4)
    average_parallel = round(sum(parallel_time_results) / NUM_TESTS, 4)
    # print(f'Sequential DFS: {average_sequential} sec')
    # print(f'Parallel DFS: {average_parallel} sec')
    # print(f'Parallel is faster {average_sequential / average_parallel} times')
    return average_sequential, average_parallel


if __name__ == '__main__':
    # children = [4, 5, 3, 4, 3, 4, 5, 3, 4]
    # height = [2, 2, 3, 3, 4, 4, 4, 5, 5]
    # for i in range(len(children)):
    #     adj_list = create_tree.create_balanced_tree(children[i], height[i])
    #     print(len(adj_list))

    number = [31, 40, 85, 121, 341, 781, 364, 1365]
    df = pd.DataFrame(columns=['# Nodes', 'Sequential time', 'Parallel time', 'Comparison'])

    for i in number:
        # call adjacency list from file by path
        path = balanced_json_path + str(i) + '_nodes.json'
        adj_list = create_tree.read_json(path)
        num_branches = len(adj_list[0])
        for j in range(NUM_TESTS):
            # calculate time in sequential
            seq_start_time = round(time.time(), 4)  # time in seconds
            sequential_dfs.dfs(adj_list, 0)
            sequential_time.append(round(time.time(), 4) - seq_start_time)

            # calculate time in parallel
            par_start_time = round(time.time(), 4)  # time in seconds
            parallel_dfs.parallel_dfs(adj_list, 0, num_branches)
            parallel_time.append(round(time.time(), 4) - par_start_time)

        # save time results in excel file
        sequential, parallel = time_results(sequential_time, parallel_time)

        df = df.append({'# Nodes': i, 'Sequential time': sequential, 'Parallel time': parallel,
                        'Comparison': sequential / parallel}, ignore_index=True)
        print(df)

    df.to_excel(excel_path, index=False)
