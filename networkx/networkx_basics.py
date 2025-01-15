import networkx as nx
import matplotlib.pyplot as plt

# Define the graph with distances
graph_dict = {
    "A": [("B", 2), ("C", 5)],
    "B": [("C", 1), ("D", 3)],
    "C": [("D", 2)],
    "D": [("E", 4)]
}

# Create an undirected graph with distances
G = nx.Graph()  # Undirected graph
for node, edges in graph_dict.items():
    for neighbor, weight in edges:
        G.add_edge(node, neighbor, weight=weight)

# Visualize the graph with weights
pos = nx.spring_layout(G)  # Positioning for visualization
nx.draw(G, pos, with_labels=True, node_color='lightgreen', font_weight='bold')
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.savefig("graph_with_distances.png")
