# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Build a dataframe with some connections
df = pd.DataFrame({'from': ['1','2','3','4'], 'to': ['3','3','4','5']})

# Build your graph
G = nx.from_pandas_edgelist(df, 'from', 'to')

# Plot it
plt.figure(figsize=(7,4))
nx.draw(G, with_labels=True, node_size=700, node_color="purple", alpha=0.5, edge_color='black')
plt.savefig("example_close_centr_theory.png")
plt.show()


