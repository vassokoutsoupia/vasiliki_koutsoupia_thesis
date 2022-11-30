# Apply clustering and show the node attributes of each community/cluster
import community
import networkx as nx
import matplotlib.pyplot as plt

# read the graph and use the label attributes (party, noitype)
from politicians_evaluation import print_metrics_cluster

G = nx.read_gexf('nois_projected_graph_overlap_attributes.gexf', relabel=True)


# the resolution parameter influences the number of communities
def experiment(res):
    part = community.best_partition(G, resolution=res)
    size = float(len(set(part.values())))
    print('> Experiment:')
    print('Resolution parameter: ', res)
    print('num of partitions: ', size)
    return part


resolution = 0.91
partition = experiment(resolution)

# sort the nodes by their community number
result = sorted(partition.items(), key=lambda item: item[1])

ground_truth_labels_dict = {}
# louvain_labels_dict = {}

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
        node = G.nodes[name]
        ground_truth_labels_dict[name] = parties_id[node['party']]
    count = count + 1

# Prepare label lists
ground_truth_labels = []
for node in G.nodes:
    ground_truth_labels.append(ground_truth_labels_dict[node])
# Ground Truth για το clustering: Το πραγματικό κόμμα κάθε βουλευτή

# Evaluation fo the quality of the clustering
print_metrics_cluster('f{resolution}', ground_truth_labels, louvain_labels)

# parties: nd, syriza, kinal, elli, mera
color_palette = ['blue', 'red', 'green', 'orange', 'cyan', 'grey']
color_map = []
for node in G:
    color_map.append(color_palette[ground_truth_labels_dict[node]])

# Canvas size
plt.figure(1, figsize=(12, 12))

# width: edge width
# node_color: List with the color of each graph node
# labels: Dictionary with the label of each node
nx.draw(G, labels=ground_truth_labels_dict, with_labels=True, node_color=color_map, width=0.1)

# nx.draw(G, with_labels=True)
plt.show()
