from algorithm.graph.mst import kruskal






edges = [
  (1,2,29),
  (1,5,75),
  (2,3,35),
  (2,6,34),
  (3,4,7),
  (4,6,23),
  (4,7,13),
  (5,6,53),
  (6,7,25)
]
vertices = [1,2,3,4,5,6,7]


assert kruskal(edges, vertices) == 159, "Incorrect"