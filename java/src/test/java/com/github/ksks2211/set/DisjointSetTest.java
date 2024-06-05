package com.github.ksks2211.set;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * @author rival
 * @since 2024-05-31
 */
class DisjointSetTest {


    @Test
    public void test1() {
        DisjointSet ds = new DisjointSet(5);


        ds.union(0,2);
        ds.union(1,2);
        ds.union(3,4);


        assertEquals(ds.find(0), ds.find(2));
        assertNotEquals(ds.find(1), ds.find(3));


        ds.union(0,4);

        assertEquals(ds.find(2),ds.find(3));

    }
}