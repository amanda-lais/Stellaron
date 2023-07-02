import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

options = {
    'edge_color': 'white',
    'node_color': 'orange',
    'node_size': 200,
    'width': 1,
    'node_shape': "*",
    'style': ':',
    'font_color': 'white',
}

aries = [(0, 1), (1, 2), (2, 3)]

G = nx.Graph()
positions = {0: [0, 0], 1: [3, -1], 2: [4, -2], 3: [4.2, -2.5]}
G.add_edges_from(aries)
ax = plt.gca().set_facecolor("black")
#ax.axis('off')
#ax = plt.figure().gca()
#ax.set_facecolor("#00000F")
#ax.set_axis_off()
nx.draw_networkx(G, positions, with_labels=False, label="The Aries Constellation", **options)
#ax.set_facecolor("#00000F")

plt.show()
