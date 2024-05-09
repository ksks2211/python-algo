from algorithm.graph.shortest_path import floyd_warshall

edges = [
  (1,2,4),
  (1,4,6),
  (2,1,3),
  (2,3,7),
  (3,1,5),
  (3,4,4),
  (4,3,2)
  ]

dist = floyd_warshall(edges,4)



dist = [ row[1:] for row in dist[1:]]
print(dist)