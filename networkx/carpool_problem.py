import networkx as nx
import matplotlib.pyplot as plt


A = [1, 1, 1, 9, 9, 9, 9, 7, 8, 10, 11, 12, 13]
B = [2, 0, 3, 1, 6, 5, 4, 0, 0, 4, 4, 4, 4]

# Create an undirected graph with distances
G = nx.Graph()  

#add edges
edges = zip(A, B)
G.add_edges_from(edges)

#source and sink
source = 5
sink = 0

#find cost of the shortest path
shortest_path = nx.shortest_path(G, source, sink, weight='weight')

#print the shortest path
print(shortest_path)

# Visualize the graph with weights
pos = nx.spring_layout(G)  # Positioning for visualization
nx.draw(G, pos, with_labels=True, node_color='lightgreen', font_weight='bold')
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.savefig("graph_with_distances.png")
