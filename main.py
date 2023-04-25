import time

import pandas as pd

import createGraph, createTree, consDFS
import random

import dfs_balanced
import par_dfs
import parallelDFS

unb_path = 'C:/Users/serg/PycharmProjects/coursework_parallel/unbalanced_adj_list/'
bal_path = 'C:/Users/serg/PycharmProjects/coursework_parallel/balanced_adj_list/'
excel_path = 'C:/Users/serg/PycharmProjects/coursework_parallel/results.xlsx'

NUM_TESTS = 4
sequential_time = []
parallel_time = []

def time_results(sequential_time_results, parallel_time_results):
    average_sequential = round(sum(sequential_time_results) / NUM_TESTS, 4)
    average_parallel = round(sum(parallel_time_results) / NUM_TESTS, 4)
    print(f'Sequential DFS: {average_sequential} sec')
    print(f'Parallel DFS: {average_parallel} sec')
    print(f'Parallel is faster {average_sequential / average_parallel} times')
    return average_sequential, average_parallel

if __name__ == '__main__':
    #createGraph.create_directed_graph(20)
    #createGraph.create_undirected_graph(10, 20)
    # children = [2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6]
    # height = [2, 3, 3, 5, 7, 3, 5, 7, 9, 4, 6, 8, 4, 6, 7]
    # for i in range(len(children)):
    #     adj_list = createTree.create_balanced_tree(children[i], height[i])

    #number = [7, 15, 40, 85, 364, 781, 1365, 1555, 3280, 19531, 21845, 349525, 488281]
    number = [40, 1555, 3280, 19531, 21845, 349525, 488281]
    #number = [50, 200, 500, 1000, 1500, 3000, 5000, 7500, 10000, 12500, 15000, 20000, 50000]
    df = pd.DataFrame(columns=['# Nodes', 'Sequential time', 'Parallel time', 'Comparison'])

    # for i in number:
    #     adj_list = createTree.create_random_tree(i)

    for i in number:
        for j in range(NUM_TESTS):
            #call adjacency list from file by path
            path = bal_path + str(i) +'_nodes.csv'
            adj_list = createTree.read_adj_list(path)

            #calculate time in sequential
            seq_start_time = round(time.time() * 1000, 4) #time in milliseconds
            consDFS.dfs(adj_list, 0)
            sequential_time.append(round(time.time() * 1000, 4) - seq_start_time)

            #calculate time in parallel
            par_start_time = round(time.time() * 1000, 4)
            #parallelDFS.parallel_dfs(adj_list, 0)
            par_dfs.parallel_dfs(adj_list, 0, 4)
            #dfs_balanced.parallel_dfs(adj_list, 4)
            parallel_time.append(round(time.time() * 1000, 4) - par_start_time)
            #parallel_time.append(1)

        #save time results in excel file
        sequential, parallel = time_results(sequential_time, parallel_time)

        df = df.append({'# Nodes': i, 'Sequential time': sequential, 'Parallel time': parallel, 'Comparison':sequential/parallel}, ignore_index=True)
        print(df)

    df.to_excel(excel_path, index=False)


    # for i in number:
    #     adj_list = createTree.create_random_tree(i)

    #
    # arr = [i for i in range(len(adj_list))]
    # random_int = random.choice(arr)
    # print(random_int)

    # visited, visited_order = consDFS.dfs(adj_list, 0)
    # print('Adjacency list:')
    # print(adj_list)
    # print('Visited:')
    # print(visited)
    # print('Order of visit: ')
    # print(visited_order)



