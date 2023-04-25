import networkx as nx
import json

balanced_json_path = 'C:/Users/serg/PycharmProjects/tpo_coursework_final/balanced_list_json/'


# Save adjacency list into JSON file as a list
# Parameters: adj_list - adjacency list as a dictionary; type - balanced or unbalanced
def save_json(adj_list, type):
    path = balanced_json_path + str(len(adj_list)) + '_nodes.json'
    my_tree = [[neighbour for neighbour in adj_list[node]] for node in adj_list]
    with open(path, 'w', newline='') as f:
        json.dump(my_tree, f)


# Read JSON file with a list
# Parameters: path - path to file
def read_json(path):
    with open(path, 'r') as f:
        adj_list = json.load(f)
    return adj_list


# Create balanced tree
# Parameters: children - amount of childen nodes for each node, levels - height of balanced tree
def create_balanced_tree(children, levels):
    tree = nx.balanced_tree(children, levels)
    adj_list = {}
    for node, neighbours in dict(tree.adjacency()).items():
        adj_list[node] = set(neighbours.keys())

    save_json(adj_list, 'bal')
    return adj_list
