package com.github.ksks2211.graph.undirected;

/**
 * @author rival
 * @since 2023-10-01
 */
public class BasicAdjacencyMatrixGraph {
    private final int vertices;
    private boolean[][] adjacencyMatrix;
    public BasicAdjacencyMatrixGraph(int vertices) {
        this.vertices = vertices;
        this.adjacencyMatrix = new boolean[vertices][vertices];
    }
    public void addEdge(int source, int destination) {
        adjacencyMatrix[source][destination] = true;
        adjacencyMatrix[destination][source] = true;
    }
    public int getSize(){
        return  this.vertices;
    }


}
