# community detection using Girvan-Newman algorithm

import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
import time
import matplotlib.cm as cm
import networkx.algorithms.community as nx_comm
from networkx import edge_betweenness_centrality as betweenness

# measure the execution time
start_time = time.time()

# open and read projected graph H
projected_graph_file = Path("C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\vasiliki_koutsoupia_thesis\\projected_H.gexf")
H = nx.read_gexf(projected_graph_file)


def print_metrics_community(method_name, H, communities):
    modularity_method = nx_comm.modularity(H, communities)
    coverage_method = nx_comm.coverage(H, communities)
    performance_method = nx_comm.performance(H, communities)
    print('---------')
    print(f'Metrics for communities with {method_name}')
    print(f'Modularity ({method_name}): {modularity_method}')
    print(f'Coverage ({method_name}: {coverage_method}')
    print(f'Performance ({method_name}: {performance_method}')

print('Girvan Newman')

# Girvan Newman community detection
num_clusters_to_find = 4
all_com = []


def most_central_edge(H):
    centrality = betweenness(H, weight="weight")
    return max(centrality, key=centrality.get)

for i in range(num_clusters_to_find):
    if H.number_of_edges() > 0:
        comp = nx.algorithms.community.centrality.girvan_newman(H, most_valuable_edge=most_central_edge)
        tup = tuple(sorted(c) for c in next(comp))
        all_com.extend(tup)
    else:
        break

print(all_com)

#print_metrics_community('Girvan Newman', H, all_com)



# make the color_map
#colors = ['blue', 'orange', 'red', 'green', 'black']

# Color nodes based on the communities
#c = [None] * len(H)
#for idx, com_set in enumerate(all_com):
#    for node in com_set:
#        c[node] = colors[idx % len(colors)]

#nx.draw(H, with_labels=True, node_color=c)
#plt.savefig("Graph_Girvan_Newman.png")
#plt.show()


# execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"execution time is: {execution_time} seconds")