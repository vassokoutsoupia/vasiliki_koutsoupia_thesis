import community
import operator
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import pandas as pd
from cdlib import algorithms
import itertools
from pathlib import Path
from networkx.algorithms.community.centrality import girvan_newman

#open and read projected graph H
projected_graph_file = Path("C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\vasiliki_koutsoupia_thesis\\nois_projected_graph_overlap_attributes.gexf")

H = nx.read_gexf(projected_graph_file)

G = nx.read_edgelist(
    "C:\\Users\\Vaso Koutsoupia\\Documents\\DOCS VASSO\\Algorithms\\twitter data set\\TEST_etoimo dataset_clustering\\2021-11-14-twitter\\2021-11-14-twitter\\user-mp.edges", delimiter=',')

print(nx.is_directed(G), nx.is_weighted(G, edge=None, weight='weight')) #FALSE ,FALSE if G has not weighted edges
print(nx.is_directed(H), nx.is_weighted(H, edge=None, weight='weight')) #FALSE ,TRUE if H has weighted edges


# Girvan-Newman Algorithm
comp = girvan_newman(H)

# make the communities into lists
node_groups = [list(c) for c in next(comp)]

print("Communities:", node_groups)

# Create the color map
color_map = []
for node in H:
    if node in node_groups[0]:
        color_map.append("red")
    else:
        color_map.append("orange")

# draw the graph with the above colors
nx.draw(H, node_color=color_map, with_labels=True)
plt.show()





# Ο κώδικας που πραγματοποιεί τα παρακάτω βήματα:
#
# Διαβάζει τον γράφο H από ένα αρχείο GEXF, αν υπάρχει. Αυτό το αρχείο περιέχει τον προβολικό γράφο του αρχικού γράφου G.
#
# Διαβάζει τον αρχικό γράφο G από ένα αρχείο ακμών (edge list). Αυτός είναι ο αρχικός γράφος που περιέχει τις ακμές μεταξύ των κόμβων (χρηστών).
#
# Ελέγχει εάν ο αρχικός γράφος G είναι διαγραφής (directed) και εάν έχει βάρη στις ακμές. Ελέγχει επίσης εάν ο προβολικός γράφος H έχει βάρη στις ακμές.
#
# Εάν ο προβολικός γράφος H δεν υπάρχει (δηλαδή, το αντίστοιχο αρχείο GEXF δεν υπάρχει), τότε δημιουργεί τον προβολικό γράφο H από τον αρχικό γράφο G. Αυτός ο γράφος H είναι ο γράφος που θα χρησιμοποιηθεί για τον αλγόριθμο Girvan-Newman.
#
# Διαβάζει πρόσθετες πληροφορίες για κάθε κόμβο από ένα αρχείο. Συγκεκριμένα, ανακτά το κόμμα του κάθε κόμβου και τον τύπο του κόμβου (εδώ, τον ρόλο "mp" για τους κόμβους που αντιστοιχούν σε μέλη του κοινοβουλίου).
#
# Εφαρμόζει τον αλγόριθμο Girvan-Newman στον προβολικό γράφο H για να εντοπίσει τις κοινότητες. Ο αλγόριθμος αυτός αφαιρεί ακμές από τον γράφο με βάση το κριτήριο του betweenness centrality των ακμών.
#
# Μετατρέπει τις κοινότητες που βρέθηκαν σε λίστες κόμβων.
#
# Δημιουργεί ένα χρωματικό χάρτη, όπου οι κόμβοι από διαφορετικές κοινότητες έχουν διαφορετικά χρώματα.
#
# Σχεδιάζει τον γράφο H με τα χρώματα των κοινοτήτων, εμφανίζοντας τις κοινότητες ως διακριτά χρωματισμένες ομάδες κόμβων.
#
# Συνοψίζοντας, ο κώδικας χρησιμοποιεί τον αλγόριθμο Girvan-Newman για τον εντοπισμό κοινοτήτων σε έναν προβολικό γράφο που δημιουργήθηκε από έναν αρχικό γράφο. Οι κοινότητες εμφανίζονται ως διακριτά χρωματισμένες ομάδες κόμβων.

