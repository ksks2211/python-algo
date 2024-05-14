from algorithm.graph.shortest_path import dijkstra, dijkstra_path






graph = {
  1:[(2,2),(3,5),(4,1)],
  2:[(3,3),(4,2)],
  3:[(2,3),(6,5)],
  4:[(3,3),(5,1)],
  5:[(3,1),(6,2)],
  6:[]
}


dijkstra(graph, 1, 5)




graph = {
    'A': [('B', 6), ('D', 1)],
    'B': [('A', 6), ('D', 2), ('E', 2), ('C', 5)],
    'C': [('B', 5), ('E', 5)],
    'D': [('A', 1), ('B', 2), ('E', 1)],
    'E': [('D', 1), ('B', 2), ('C', 5)]
}

route = dijkstra_path(graph,'A','E')

print(route)