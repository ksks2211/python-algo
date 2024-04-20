import networkx as nx


G = nx.Graph()
G.add_edge("A", "B")
G.add_edge("B", "C")

# Compute shortest path
shortest_path = nx.shortest_path(G, "A", "C")
print("Shortest path from A to C:", shortest_path)