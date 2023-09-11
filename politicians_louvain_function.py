# Apply clustering and show the node attributes of each community/cluster
import community
import networkx as nx
import matplotlib.pyplot as plt
from politicians_evaluation import print_metrics_cluster
import time


# measure the execution time
start_time = time.time()

# read projected graph H
H = nx.read_gexf('nois_projected_graph_overlap_attributes.gexf', relabel=True)

# Evaluation fo the quality of the clustering
# the resolution parameter influences the number of communities
def experiment(resolution):
    partition = community.best_partition(H, resolution=resolution)
    size = float(len(set(partition.values())))
    print('> Experiment:')
    print('Resolution parameter: ', resolution)
    print('num of partitions: ', size)
    return partition

# try resolution and make the partition
partition = experiment(0.91)

# sort the nodes by their community number
result = sorted(partition.items(), key=lambda item: item[1])

# Ground Truth for clustering: mp's real party
ground_truth_labels_dict = {}

# make the louvain's dict
louvain_labels_dict = partition
louvain_labels = [c for c in partition.values()]

# Dictionary with parties
parties = {'nd', 'syriza', 'kinal', 'elli', 'mera'}
zip_iterator = zip(parties, range(5))
parties_id = dict(zip_iterator)


# Get information for each node
count = 0
for com in set(partition.values()):
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    for name in list_nodes:
        node = H.nodes[name]
        ground_truth_labels_dict[name] = parties_id[node['party']] #username : party id

        if 'party' in node.keys():
            print(count, ',', name, ',', node['party'])
        else:
            print(count, ',', name, ',', 'NO PARTY')
            print(f'Warning: Node {node} has no label')

        if 'noitype' in node.keys():
            print(count, ", ", name, ", ", node['noitype'])
        else:
            print(count, ',', name, ',', 'NO NOITYPE')
    count = count + 1


# Prepare label lists
ground_truth_labels = []
for node in H.nodes:
    ground_truth_labels.append(ground_truth_labels_dict[node])


# function returns a dict with all the metrics for a specific resolution
def specific_res(H, resolution):
    metrics = print_metrics_cluster('f{resolution}', ground_truth_labels, louvain_labels)
    return metrics


# louvain's metrics
metrics_specific_res = specific_res(H, 0.91)
print(metrics_specific_res)
# return the value of the mutual info score
mutual_info = metrics_specific_res['mi_score']
print('mutual info score is =', mutual_info)

# draw graph after clustering
color_palette = ['blue', 'red', 'green', 'orange', 'cyan', 'grey']
color_map = []
for node in H:
    color_map.append(color_palette[partition[node]])

# Canvas size
plt.figure(1, figsize=(12, 12))
# width: edge width
# node_color: List with the color of each graph node
# labels: Dictionary with the label of each node
nx.draw(H, labels=louvain_labels_dict, with_labels=True, node_color=color_map, width=0.1)
plt.savefig("Graph_Louvain.png")
plt.show()


# execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"execution time is: {execution_time} seconds")