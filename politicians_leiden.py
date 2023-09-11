# community detection using leiden algorithm
import networkx as nx
from cdlib import algorithms
from pathlib import Path
import time

# measure the execution time
start_time = time.time()


# folder = '.'

# open and real the original graph G
G = nx.read_edgelist(
    "C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges", delimiter=',')

# open and read projected graph H
projected_graph_file = Path("C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\vasiliki_koutsoupia_thesis\\projected_H.gexf")
H = nx.read_gexf(projected_graph_file)


print(nx.is_directed(G), nx.is_weighted(G, edge=None, weight='weight')) #FALSE ,FALSE if G has not weighted edges
print(nx.is_directed(H), nx.is_weighted(H, edge=None, weight='weight')) #FALSE ,TRUE if H has weighted edges

# execute leiden algorithm for community detection
communities = algorithms.leiden(H)

# Print the communities
for i, community in enumerate(communities.communities):
    print(f"Community {i + 1}:")
    for node in community:
        print(node)

# execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"execution time is: {execution_time} seconds")