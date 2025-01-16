import networkx as nx
import matplotlib.pyplot as plt


A = [1, 1, 1, 9, 9, 9, 9, 7, 8]
B = [2, 0, 3, 1, 6, 5, 4, 0, 0]

# Create an undirected graph with distances
G = nx.Graph()  

#add edges
edges = zip(A, B)
print(edges)
G.add_edges_from(edges)

#source and sink
source = 1
sink = 0

# Visualize the graph with weights
pos = nx.spring_layout(G)  # Positioning for visualization
nx.draw(G, pos, with_labels=True, node_color='lightgreen', font_weight='bold')
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.savefig("graph_with_distances.png")
