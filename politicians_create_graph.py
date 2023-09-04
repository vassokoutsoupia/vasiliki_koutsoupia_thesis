#import community
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

from pathlib import Path

folder = '.'

projected_graph_file = Path("nois_projected_graph_overlap_attributes.gexf")

#create G
G = nx.read_edgelist("C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges", delimiter=',')

if not projected_graph_file.is_file():
 
    G = nx.read_edgelist("C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\twitter_dataset2021\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges", delimiter=',')
    print(f'Number of edges: {nx.number_of_edges(G)}')

    #check if graph is bipartite
    print(f'Graph is bipartite: {bipartite.is_bipartite(G)}')

    #obtain node set
    users, noi = bipartite.sets(G)

    print('users:', len(users))
    print('noi:', len(noi))

    #projected graph
    H = bipartite.overlap_weighted_projected_graph(G, noi, jaccard=False)

    # read auxiliary information: party of each node
    noi_list = list()
    party = {}
    node_type = {}
    with open(folder + '\\' + 'mp-all-parties.txt', 'r') as f:
        for i, line in enumerate(f):
            tokens = line.split()
            noi = tokens[0].strip()
            noi_list.append(noi)
            party[noi] = tokens[1].strip()
            node_type[noi] = 'mp'

    # store information as node attributes
    nx.set_node_attributes(H, party, 'party')
    nx.set_node_attributes(H, node_type, 'noitype')

    #write projected graph
    nx.write_gexf(H, projected_graph_file)
else:
    #create H
    H = nx.read_gexf(projected_graph_file)

print(H.number_of_edges())
print(H.number_of_nodes())

#lets find who mp exists in H
lista = []
lista = H.nodes(data=('party'))
print(lista)

list_syriza = [t[0] for t in lista if t[1] == 'syriza']
list_nd = [t[0] for t in lista if t[1] == 'nd']
list_mera = [t[0] for t in lista if t[1] == 'mera']
list_kinal = [t[0] for t in lista if t[1] == 'kinal']
list_elli = [t[0] for t in lista if t[1] == 'elli']
print('οι βουλευτές/τριες του ΣΥΡΙΖΑ', list_syriza)
print('οι βουλευτές/τριες της ΝΔ', list_nd)
print('οι βουλευτές/τριες του ΜΕΡΑ25', list_mera)
print('οι βουλευτές/τριες του ΚΙΝΑΛ', list_kinal)
print('οι βουλευτές/τριες του ΕΛ.ΛΥΣΗ', list_elli)

# save the lists of mps' names that exist in graph H, at some .xtx files
file_name = "list_syriza.txt"
file_name2 = "list_nd.txt"
file_name3 = "list_mera.txt"
file_name4 = "list_kinal.txt"
file_name5 = "list_elli.txt"

#open files and write every line of each lists
with open(file_name, "w") as file:
    for item in list_syriza:
        file.write(item + "\n")

with open(file_name2, "w") as file:
    for item in list_nd:
        file.write(item + "\n")

with open(file_name3, "w") as file:
    for item in list_mera:
        file.write(item + "\n")

with open(file_name4, "w") as file:
    for item in list_kinal:
        file.write(item + "\n")

with open(file_name5, "w") as file:
    for item in list_elli:
        file.write(item + "\n")


#draw the projection graph
plt.figure(figsize=(12,11))
nx.draw(H)
plt.savefig("Graph_projected.png")
plt.show()

#save in gexf file the graph H after the changings
output_file_name = "projected_H.gexf"
nx.write_gexf(H, output_file_name)