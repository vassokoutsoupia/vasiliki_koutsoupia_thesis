import operator
import networkx as nx
from pathlib import Path

# open and read projected graph H
projected_graph_file = Path("C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\vasiliki_koutsoupia_thesis\\projected_H.gexf")
H = nx.read_gexf(projected_graph_file)

G = nx.read_edgelist(
    "C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges", delimiter=',')

# print(H.nodes.items) #PAIRNW TA NODES, XWRIS ATTR
# print(nx.is_directed(G), nx.is_weighted(G, edge=None, weight='weight')) #FALSE ,FALSE if G has not weighted edges
# print(nx.is_directed(H), nx.is_weighted(H, edge=None, weight='weight')) #FALSE ,TRUE if H has weighted edges

# Centralities
# Degree
degCent = nx.degree_centrality(G)
print('degree:', sorted(degCent.items(), key=operator.itemgetter(1), reverse=True)[0:10])

# Computing the distance attribute
for (u, v) in H.edges():
    w = H.edges[u, v]['weight']
    H.edges[u, v]['distance'] = 1/w

# Closeness
closeCent = nx.closeness_centrality(H, u=None, distance='distance', wf_improved=True)
print('closeness:', sorted(closeCent.items(), key=operator.itemgetter(1), reverse=True)[0:10])

# Betweenness
btwnCent = nx.betweenness_centrality(H, normalized=True, weight='weight', endpoints=False)
print('betweenness:', sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[0:10])

# PageRank
pageCent = nx.pagerank(H, alpha=0.85, weight='weight')
print('pagerank:', sorted(pageCent.items(), key=operator.itemgetter(1), reverse=True)[0:10])

# Eingenvector
eigenCent = nx.eigenvector_centrality(H, weight='weight')
print('eigenvector:', sorted(eigenCent.items(), key=operator.itemgetter(1), reverse=True)[0:10])

