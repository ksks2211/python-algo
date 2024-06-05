package com.github.ksks2211.set;

/**
 * @author rival
 * @since 2024-05-31
 */
public class DisjointSet {


    private final int[] parent;

    private final int[] rank;



    public DisjointSet(int size) {
        parent = new int[size];
        rank = new int[size];

        for (int i = 0; i < size; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }



    public int find(int x) {
        if(parent[x]!=x){
            parent[x] = find(parent[x]);
        }

        return parent[x];
    }


    public void union(int a, int b) {
        int rootX = find(a);
        int rootY = find(b);

        if(rootX!=rootY){
            if(rank[rootX]>rank[rootY]){
                parent[rootY] = rootX;
            }else if(rank[rootX]<rank[rootY]){
                parent[rootX] = rootY;
            }else{
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
}
