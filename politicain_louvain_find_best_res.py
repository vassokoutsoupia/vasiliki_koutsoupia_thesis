# παραδειγμα αυτοποιησης για να βρουμε το καλυτερο resolution για το καλυτερο clustering
import numpy as np
# Apply clustering and show the node attributes of each community/cluster
import community
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# read the graph and use the label attributes (party, noitype)
from politicians_evaluation import print_metrics_cluster

G = nx.read_gexf('nois_projected_graph_overlap_attributes.gexf', relabel=True)


# the resolution parameter influences the number of communities
def experiment(resolution):
    partition = community.best_partition(G, resolution=resolution)
    size = float(len(set(partition.values())))
    # print('> Experiment:')
    # print('Resolution parameter: ', resolution)
    # print('num of partitions: ', size)
    return partition


def louvainCreator(resolution):
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
            ground_truth_labels_dict[name] = parties_id[node['party']]  # username : party id
            # if 'party' in node.keys():
            #     print(count, ',', name, ',', node['party'])
            # else:
            #     print(count, ',', name, ',', 'NO PARTY')
            #     print(f'Warning: Node {node} has no label')
            #
            # if 'noitype' in node.keys():
            #     print(count, ", ", name, ", ", node['noitype'])
            # else:
            #     print(count, ',', name, ',', 'NO NOITYPE')
        count = count + 1
    # Prepare label lists
    ground_truth_labels = []
    for node in G.nodes:
        ground_truth_labels.append(ground_truth_labels_dict[node])

    return {
        "groundTruths": ground_truth_labels,
        "louvainLabels": louvain_labels
    }


# Ground Truth για το clustering: Το πραγματικό κόμμα κάθε βουλευτή

# Evaluation fo the quality of the clustering
# function returns a dict with all the metrics
def specific_res(G,ground_truth_labels,louvain_labels):
    metrics = print_metrics_cluster('f{resolution}', ground_truth_labels, louvain_labels)
    return metrics


# TEST

low = 0.5
high = 2.0
step = 0.15  # k=10

float_res_array = np.arange(low, high, step)
float_res_list = list(float_res_array)

sorted_res_list = sorted(float_res_list)

best_res = None
best_metric = None
for res in float_res_array:
    parametersForCurrentRes = louvainCreator(res)
    metrics_specific_res = specific_res(G,parametersForCurrentRes["groundTruths"],parametersForCurrentRes["louvainLabels"])
    # print(metrics_specific_res)

    mutual_info = metrics_specific_res['mi_score']
    if best_res == None:
        best_res = res
        best_metric = mutual_info
    elif mutual_info < best_metric:
        best_metric = mutual_info
    elif mutual_info > best_metric:
        break
    # print("===============================Metrics for ", res," ==============================")
print("Best res is %s and best metric is %s" %(res,best_metric))

# print(sorted_res_list)


# # return the value of the mutual info score
#
# color_palette = ['blue', 'red', 'green', 'orange', 'cyan', 'grey']
# color_map = []
# for node in G:
#     color_map.append(color_palette[ground_truth_labels_dict[node]])
#
# # Canvas size
# plt.figure(1, figsize=(12, 12))
#
# # width: edge width
# # node_color: List with the color of each graph node
# # labels: Dictionary with the label of each node
# nx.draw(G, labels=ground_truth_labels_dict, with_labels=True, node_color=color_map, width=0.1)
# plt.savefig("Graph_Louvain.png")
#
# # nx.draw(G, with_labels=True)
# plt.show()




