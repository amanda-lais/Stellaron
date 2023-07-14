import networkx as nx
import matplotlib.pyplot as plt
import stellarinfo

# === FUNCTIONS ===

# Makes and shows graph
def gen_graph(positions, lines):
    options = {
        'edge_color': 'white',
        'node_color': 'orange',
        'node_size': 100,
        'width': 1,
        'node_shape': "*",
        'style': ':',
        'font_color': 'white',
    }
    G = nx.Graph()
    G.add_edges_from(lines)
    nx.draw_networkx(G, positions, with_labels=False, **options)
    ax = plt.gca().set_facecolor("black")
    plt.show()

# Sends some constellation
# parameters to gen_graph
def ct_graph(n):
    ct_lines = stellarinfo.get_lines(n)[0]
    pos = stellarinfo.ct_pos(n)
    gen_graph(pos, ct_lines)