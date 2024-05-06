from algorithm.graph import traversal



graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}


graph2 = {
    1 : [2,3,8],
    2 : [1,7],
    3 : [1,4,5],
    4:[3,5],
    5:[3,4],
    6:[7],
    7:[2,6,8],
    8:[1,7]
    
}

print("\nDFS : ")
traversal.dfs_recursive(graph2,1)  


print("\nDFS : ")
traversal.dfs_iterative(graph2,1)


print("\nBFS : ")
traversal.bfs(graph2, 1)