from algorithm.graph.shortest_path import dijkstra






graph = {
  1:[(2,2),(3,5),(4,1)],
  2:[(3,3),(4,2)],
  3:[(2,3),(6,5)],
  4:[(3,3),(5,1)],
  5:[(3,1),(6,2)],
  6:[]
}


dijkstra(graph, 1, 5)


