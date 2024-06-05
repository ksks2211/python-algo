package com.github.ksks2211.search;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * @author rival
 * @since 2024-05-31
 */
class BinarySearchTest {

    @Test
    void binarySearch() {
        int[] arr = {1,2,3,4,5,6,7,8,9,9,9,10};
        assertEquals(8 , BinarySearch.findLeftMost(arr,9));
        assertEquals(-1, BinarySearch.bisectLeft(arr,11));
        assertEquals(10,BinarySearch.findRightMost(arr,9) );
        assertEquals(3, BinarySearch.count(arr,9));
    }
}