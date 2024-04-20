package com.github.ksks2211.sorting;
import java.util.Arrays;
import java.util.Random;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * @author rival
 * @since 2023-09-30
 */
class IntArraySorterTest {

    private final Random RANDOM = new Random();
    public int[] generateRandomIntArray(int max, int size) {
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = RANDOM.nextInt(max + 1);  // nextInt(n) returns values between 0 (inclusive) and n (exclusive)
        }
        return array;
    }

    @DisplayName("1. selection sort")
    @Test
    void test_1() {
        int[] arr= generateRandomIntArray(20,10);
        IntArraySorter.selectionSort(arr);
        Assertions.assertTrue(IntArraySorter.isSorted(arr));
    }

    @DisplayName("2. insertion sort")
    @Test
    void test_2(){
        int[] arr= generateRandomIntArray(20,10);
        IntArraySorter.insertionSort(arr);
        Assertions.assertTrue(IntArraySorter.isSorted(arr));

    }

    @DisplayName("3. bubble sort")
    @Test
    void test_3(){
        int[] arr= generateRandomIntArray(20,10);
        IntArraySorter.bubbleSort(arr);
        Assertions.assertTrue(IntArraySorter.isSorted(arr));
    }

    @DisplayName("4. shell sort")
    @Test
    void test_4(){
        int[] arr= generateRandomIntArray(20,10);
        IntArraySorter.shellSort(arr);
        Assertions.assertTrue(IntArraySorter.isSorted(arr));

    }



    @DisplayName("5. quick sort")
    @Test
    void test_5() {
        int[] arr = generateRandomIntArray(20, 10);
        IntArraySorter.quickSort(arr);
        Assertions.assertTrue(IntArraySorter.isSorted(arr));
    }



    @DisplayName("6. heap sort")
    @Test
    void test_6(){
        int[] arr = generateRandomIntArray(20,10);
        IntArraySorter.heapSort(arr);
        Assertions.assertTrue(IntArraySorter.isSorted(arr));
        System.out.println(Arrays.toString(arr));
    }


    @DisplayName("7. merge sort")
    @Test
    void test_7(){
        System.out.println("Merge Sort");
        int[] arr = generateRandomIntArray(20,10);
        IntArraySorter.mergeSort(arr);
        Assertions.assertTrue(IntArraySorter.isSorted(arr));
        System.out.println(Arrays.toString(arr));
    }





}