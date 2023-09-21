# clustering using the louvain algorithm

import community
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from politicians_evaluation import print_metrics_cluster
import time

# measure the execution time
start_time = time.time()


# read projected graph
H = nx.read_gexf('nois_projected_graph_overlap_attributes.gexf', relabel=True)

ground_truth_labels_dict = {}
louvain_labels_dict = {}

# functions
def experiment(resolution):
    partition = community.best_partition(H, resolution=resolution)
    size = float(len(set(partition.values())))
    print('> Experiment:')
    print('Resolution parameter: ', resolution)
    print('num of partitions: ', size)
    return partition


def louvainCreator(resolution):
    partition = experiment(resolution)
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
            ground_truth_labels_dict[name] = parties_id[node['party']]  # username : party id
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

    # Ground Truth for clustering: the mp's real party
    # Prepare label lists
    ground_truth_labels = []
    for node in H.nodes:
        ground_truth_labels.append(ground_truth_labels_dict[node])

    # return a dict with 2 lists, ground truth labels and louvain labels
    return {
        "groundTruths": ground_truth_labels,
        "louvainLabels": louvain_labels, "partition":partition
    }


# Evaluation fo the quality of the clustering
def specific_res(H,ground_truth_labels, louvain_labels):
    metrics = print_metrics_cluster('f{resolution}', ground_truth_labels, louvain_labels)
    return metrics


# ##################### start ######################## #

low = 0.5
high = 2.0
k = 10
step = (high-low)/k
i = 1

float_res_array = np.arange(low, high, step)
float_res_list = list(float_res_array)
sorted_res_list = sorted(float_res_list)


metrics_specific_res = None
best_res = None
best_metric = None

while i <= 5:


    for res in float_res_array:
        parametersForCurrentRes = louvainCreator(res)
        metrics_specific_res = specific_res(H, parametersForCurrentRes["groundTruths"], parametersForCurrentRes["louvainLabels"])
        normalized_mutual_info = metrics_specific_res['nmi_score']

        if best_res == None:
            best_res = res
            best_metric = normalized_mutual_info
        elif normalized_mutual_info > best_metric:
            best_res = res
            best_metric = normalized_mutual_info


    low = best_res - step
    high = best_res + step
    step = (high - low) / k

    float_res_array = np.arange(low, high, step)
    float_res_list = list(float_res_array)
    sorted_res_list = sorted(float_res_array) # resolutions list
    i = i + 1

if best_res is not None:
    best_partition = louvainCreator(best_res)["partition"]
    louvain_labels_dict = best_partition


print("Best resolution is %s,metrics are %s and the best metric (NMI) is %s" % (best_res, metrics_specific_res, best_metric))
print("sortred resolution list:", sorted_res_list)
print("modularity is", modularity)

#sorted_items = sorted(louvain_labels_dict.items(), key=lambda item: item[1])
# Print the labels and values one by one
#for label, value in sorted_items:
#    print(f'mp: {label}, community: {value}')

# draw H
color_palette = ['blue', 'red', 'green', 'orange', 'cyan', 'grey']
color_map = []
for node in H:
    color_map.append(color_palette[louvain_labels_dict[node]])

# Canvas size
plt.figure(1, figsize=(12, 12))

# width: edge width
# node_color: List with the color of each graph node
# labels: Dictionary with the label of each node
nx.draw(H, labels=louvain_labels_dict, with_labels=True, node_color=color_map, width=0.1)
plt.savefig("Graph_Louvain_find_best_res.png")
plt.show()

# execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"execution time is: {execution_time} seconds")


