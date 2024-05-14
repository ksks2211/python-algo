from algorithm.graph.dag import topological_sort

graph = [
    [],
    [],
    [3],
    [1],
    [0, 1],
    [0, 2],
]

vertices = [0,1,2,3,4,5]

print(topological_sort(graph, vertices))


graph = {
  1 : [2,5],
  2 : [3,6],
  3 : [4],
  4 : [7],
  5 : [6],
  6 : [4],
  7 : []
}


vertices = [1,2,3,4,5,6,7]

print(topological_sort(graph, vertices))