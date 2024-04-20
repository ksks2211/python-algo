package com.github.ksks2211.sorting;

import java.util.Arrays;

/**
 * @author rival
 * @since 2023-09-30
 */
public class IntArraySorter {
    private static void swap(int[] arr, int i, int j) {
        if (i == j) return;

        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }



    // Bubble Sort
    public static void bubbleSort(int[] arr) {
        boolean isSorted;
        for (int i = 0; i < arr.length; i++) {

            isSorted = true;
            for (int j = 0; j < arr.length - i - 1; j++) {
                if(arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                    isSorted = false;
                }
            }
            if(isSorted)break;
        }
    }

    // Selection Sort

    public static void selectionSort(int[] arr) {
        int min_index;
        for (int i = 0; i < arr.length - 1; i++) {
            min_index = i;

            // Select index of smallest number
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[min_index]) {
                    min_index = j;
                }
            }
            swap(arr, i, min_index);
        }
    }


    // Insertion Sort
    public static void insertionSort(int[] arr) {
        int key, j;

        for (int i = 1; i < arr.length; i++) {
            // Remember new element
            key = arr[i];

            // Move
            for (j = i-1; j >= 0 && arr[j] > key; j--) {
                arr[j+1] = arr[j];
            }

            arr[j+1] = key;
        }
    }


    // Shell Sort
    public static void shellSort(int[] arr){
        for(int gap=arr.length/2;gap>0;gap/=2){
            insertionSortWithGap(arr,gap);
        }
    }

    private static void insertionSortWithGap(int[] arr, int gap){

        int key, j;


        for(int i=gap; i<arr.length ; i++){
            key = arr[i];
            for(j=i; j>=gap && arr[j-gap] > key; j-=gap){
                arr[j] = arr[j-gap];
            }
            if(i!= j)arr[j] = key;
        }
    }



    // Quick Sort
    public static void quickSort(int[] arr){
        quickSort(arr, 0, arr.length-1);
    }

    private static void quickSort(int[] arr, int low, int high){
        if(low < high){
            int pivotIndex = partition(arr, low, high);
            quickSort(arr,low, pivotIndex-1);
            quickSort(arr,pivotIndex+1, high);
        }
    }


    // Partition and return pivotIndex
    private static int partition(int[] arr, int low, int high){
        int pivot = arr[high];

        int i = low -1;

        for(int j=low; j<high;j++){
            if(arr[j]<=pivot){
                i++;
                swap(arr,i,j);
            }
        }


        swap(arr,i+1,high);
        return i+1;
    }

    // Heap Sort
    public static void heapSort(int[] arr){
        // Heapify to Max-Heap
        for(int i = arr.length/2 -1 ;i >=0 ; i--){
            maxHeapify(arr,i,arr.length);
        }


        //
        for(int size = arr.length-1 ; size >0 ; size--){
          swap(arr,size,0);
          maxHeapify(arr,0,size);
        }
    }

    private static void maxHeapify(int[] arr, int curIdx, int size){

        int maxIdx,leftIdx,rightIdx;

        while ((leftIdx=2*curIdx+1)<size) {
            maxIdx = curIdx;
            rightIdx = leftIdx+1;

            if (arr[leftIdx] > arr[maxIdx]) {
                maxIdx = leftIdx;
            }

            if (rightIdx < size && arr[rightIdx] > arr[maxIdx]) {
                maxIdx = rightIdx;
            }

            if (curIdx == maxIdx) break;

            swap(arr, curIdx, maxIdx);
            curIdx = maxIdx;
        }
    }


    // Merge Sort

    public static void mergeSort(int[] arr){
        mergeSort(arr,0,arr.length-1);
    }


    private static void mergeSort(int[] arr, int left, int right){
        if(left<right){
            int middle = left + (right-left)/2;
            mergeSort(arr,left,middle);
            mergeSort(arr,middle+1,right);
            merge(arr,left,middle,right);
        }
    }


    private static void merge(int[] arr, int left, int middle, int right){

        int leftArrSize = middle - left +1;
        int rightArrSize = right - middle;

        int[] leftArr = Arrays.copyOfRange(arr,left,middle+1);
        int[] rightArr = Arrays.copyOfRange(arr,middle+1,right+1);

        int i=0,j=0,k=left;


        while(i<leftArrSize && j <rightArrSize){
            if(leftArr[i]<=rightArr[j]){
                arr[k] = leftArr[i];
                i++;
            }else{
                arr[k] = rightArr[j];
                j++;
            }
            k++;
        }

        while(i < leftArrSize){
            arr[k++] = leftArr[i++];
        }

        while(j < rightArrSize){
            arr[k++] = rightArr[j++];
        }
    }


    public static boolean isSorted(int[] array) {
        for (int i = 1; i < array.length; i++) {
            if (array[i - 1] > array[i]) {
                return false;
            }
        }
        return true;
    }
}
