import csv

import networkx as nx
from matplotlib import pyplot as plt
import pandas as pd

plot_path = '/not used data/plots/123'
matr_csv_path = '/not used data/adj_matrix/'
list_csv_path = '/not used data/adj_lists/'
balanced_path = 'C:/Users/serg/PycharmProjects/coursework_parallel/balanced_adj_list/'
unbalanced_path = 'C:/Users/serg/PycharmProjects/coursework_parallel/unbalanced_adj_list/'
nx_unb_plot_path = '/not used data/nx_unb_plot/'
nx_bal_plot_path = '/not used data/nx_bal_plot/'


def plot_save(graph, type):  # TODO: fix plotting
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    print('Number of nodes: ' + str(num_nodes))
    print('Number of edges: ' + str(num_edges))

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.savefig(plot_path + str(num_nodes) + '_nodes_' + type + '.jpg')
    plt.show()
    print('Plot saved')


def print_matrix(adj_matrix, adj_list):
    print("Adjacency Matrix:")
    print(adj_matrix)
    print("Adjacency List:")
    print(adj_list)


def save_adjacency(adj_matrix, adj_list):
    matr_path = matr_csv_path + str(len(adj_list)) + '_nodes.csv'
    list_path = list_csv_path + str(len(adj_list)) + '_nodes.csv'
    print(matr_path)
    print(list_path)
    adj_matrix.to_csv(matr_path)
    adj_list.to_csv(list_path)


def save_adj_list(adj_list, type):
    if type == 'bal':
        path = balanced_path + str(len(adj_list)) + '_nodes.csv'
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['node', 'neighbours'])
            for node, neighbours in adj_list.items():
                writer.writerow([node, ','.join(str(n) for n in neighbours)])
    else:
        path = unbalanced_path + str(len(adj_list)) + '_nodes.csv'
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['node', 'neighbours'])
            for node, neighbours in adj_list.items():
                writer.writerow([node, ','.join(str(n) for n in neighbours)])


def create_random_tree(size):
    tree = nx.random_tree(size)
    adj_list = {}
    for node, neighbours in dict(tree.adjacency()).items():
        adj_list[node] = set(neighbours.keys())
    # adj_list = dict(tree.adjacency())
    # df_adj_list = pd.DataFrame(adj_list.items(), columns=['node', 'neighbours'])
    #nx.write_network_text(tree, sources=[0])

    # adj_matrix = nx.to_numpy_array(tree)
    # df_adj_matrix = pd.DataFrame(adj_matrix, columns=range(size), index=range(size))
    #
    # print_matrix(df_adj_matrix, df_adj_list)
    # graph = nx.Graph(adj_list)
    # plot_save(graph, 'dir')
    save_adj_list(adj_list, 'unbal')
    return adj_list


def create_balanced_tree(children, levels):
    tree = nx.balanced_tree(children, levels)
    adj_list = {}
    for node, neighbours in dict(tree.adjacency()).items():
        adj_list[node] = set(neighbours.keys())

    save_adj_list(adj_list, 'bal')
    return adj_list



    #print('Adjacency list: ')
    #print(adj_list)
    #df_adj_list = pd.DataFrame(adj_list.items(), columns=['node', 'neighbours'])
    # nx.write_network_text(tree, sources=[0]) #!!!
    # path = nx_bal_plot_path + str(len(adj_list)) + '_nodes_tree.txt'
    # with open(path, 'w') as f:
    #     nx.write_edgelist(tree, f)

    #save_adj_list(df_adj_list, 'bal')
    #return adj_list

def read_adj_list(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        adj_list = {}
        next(reader) #ignore first line
        for row in reader:
            node = int(row[0])
            neighbors = {int(n) for n in row[1].split(',') if n}
            adj_list[node] = neighbors

    return adj_list
