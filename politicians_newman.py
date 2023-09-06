import community
import operator
import networkx as nx
import matplotlib.pyplot as plt
from cdlib import algorithms
import itertools
from pathlib import Path
from networkx.algorithms.community.centrality import girvan_newman

# open and read projected graph H
projected_graph_file = Path("C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\vasiliki_koutsoupia_thesis\\projected_H.gexf")
H = nx.read_gexf(projected_graph_file)

G = nx.read_edgelist(
    "C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges", delimiter=',')

# print(nx.is_directed(G), nx.is_weighted(G, edge=None, weight='weight')) #FALSE ,FALSE if G has not weighted edges
# print(nx.is_directed(H), nx.is_weighted(H, edge=None, weight='weight')) #FALSE ,TRUE if H has weighted edges

# Girvan-Newman Algorithm
comp = girvan_newman(H)

# make the communities into lists
node_groups = [list(c) for c in next(comp)]

print("Communities:", node_groups)

# Create the color map
color_map = []
for node in H:
    if node in node_groups[0]:
        color_map.append("blue")
    elif node in node_groups[1]:
        color_map.append("orange")
    elif node in node_groups[2]:
        color_map.append("red")
    elif node in node_groups[3]:
        color_map.append("green")
    else:
        color_map.append("black")

# draw the graph with the above colors
nx.draw(H, node_color=color_map, with_labels=True)
plt.savefig("Graph_Girvan_Newman.png")
plt.show()