from algorithm.graph.cycle import has_cycle






# cycled
edges = [
    (1,4),
    (2,4),
    (2,5),
    (4,5),
    (3,5)
]


assert has_cycle([1,2,3,4,5], edges) == True

# un-cycled
edges = [
    (1,4),
    (2,5),
    (4,5),
    (3,5)
]

assert has_cycle([1,2,3, 4,5], edges) == False


