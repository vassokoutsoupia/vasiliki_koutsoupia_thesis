# import community
import operator
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

from pathlib import Path

folder = '.'

projected_graph_file = Path("nois_projected_graph_overlap_attributes.gexf")

if not projected_graph_file.is_file():

    G = nx.read_edgelist(
        "C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\TEST_etoimo dataset_clustering\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges",
        delimiter=',')

    print(f'Number of edges: {nx.number_of_edges(G)}')

    # check if graph is bipartite
    print(f'Graph is bipartite: {bipartite.is_bipartite(G)}')

    # obtain node set
    users, nopi = bipartite.sets(G)

    print('users:', len(users))
    print('nopi:', len(nopi))

    # projected graph
    H = bipartite.overlap_weighted_projected_graph(G, nopi, jaccard=False)

    # read auxiliary information: party of each node
    noi_list = list()
    party = {}
    node_type = {}
    with open(folder + '\\' + 'mp-of-all-parties.txt', 'r') as f:
        for i, line in enumerate(f):
            tokens = line.split()
            noi = tokens[0].strip()
            noi_list.append(noi)
            party[noi] = tokens[1].strip()
            node_type[noi] = 'mp'

    # store information as node attributes
    nx.set_node_attributes(H, party, 'party')
    nx.set_node_attributes(H, node_type, 'noitype')

    # write projected graph
    nx.write_gexf(H, projected_graph_file)


else:
    H = nx.read_gexf(projected_graph_file)


G = nx.read_edgelist(
    "C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\TEST_etoimo dataset_clustering\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges",
    delimiter=',')

#print(H.nodes.items) #PAIRNW TA NODES, XWRIS ATTR
#print(nx.is_directed(G), nx.is_weighted(G, edge=None, weight='weight')) #FALSE ,FALSE if G has not weighted edges
#print(nx.is_directed(H), nx.is_weighted(H, edge=None, weight='weight')) #FALSE ,TRUE if H has weighted edges



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

# betweenness
btwnCent = nx.betweenness_centrality(H, normalized=True, weight='weight', endpoints=False)
print('betweenness:', sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[0:10])

# PageRank
pageCent = nx.pagerank(H, alpha=0.85, weight='weight')
print('pagerank:', sorted(pageCent.items(), key=operator.itemgetter(1), reverse=True)[0:10])

# Eingenvector
eigenCent = nx.eigenvector_centrality(H, weight='weight')
print('eigenvector:', sorted(eigenCent.items(), key=operator.itemgetter(1), reverse=True)[0:10])

# DRAW THE PROJECTION GRAPH
plt.figure(figsize=(12, 11))
nx.draw(H)
plt.savefig("Graph_projected.png")
plt.show()