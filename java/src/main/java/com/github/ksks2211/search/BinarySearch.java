package com.github.ksks2211.search;

/**
 * @author rival
 * @since 2024-05-31
 */
public class BinarySearch {


    public static int findLeftMost(int[] arr, int target){
        int left = 0;
        int right = arr.length - 1;
        int result = -1;


        while(left <= right){
            int mid = left + (right - left) / 2;

            if(arr[mid] == target){
                result = mid;
                right = mid - 1;
            }
            else if(arr[mid] < target){
                left = mid + 1;
            }else {
                right = mid - 1;
            }
        }

        return result;


    }
    public static int findRightMost(int[] arr, int target){
        int left = 0;
        int right = arr.length - 1;

        int result = -1;

        while(left <= right){
            int mid = left + (right - left) / 2;

            if(arr[mid] == target){
                result = mid;
                left = mid + 1;
            }else if(arr[mid] > target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }

        }


        return result;
    }




    public static int bisectLeft(int[] arr, int target){
        int left = 0;
        int right = arr.length - 1;

        return bisectLeft(arr, target, left, right);
    }



    private static int bisectLeft(int[] arr, int target, int left, int right){

        if (left > right) return -1;

        int mid = left + (right - left) / 2;



        if( arr[mid] == target && (mid==left || target > arr[mid-1])){
          return mid;
        }


        if(arr[mid] >= target){
            return bisectLeft(arr, target, left, mid - 1);
        }else{
            return bisectLeft(arr, target, mid + 1, right);
        }


    }


    public static int bisectRight(int[] arr, int target){

        int left = 0;
        int right = arr.length - 1;
        return bisectRight(arr,target, left, right);
    }

    private static int bisectRight(int[] arr, int target, int left, int right) {

        if (left > right) return -1;

        int mid = left + (right - left) / 2;

        if(arr[mid] == target && (mid==right || target < arr[mid+1])){
            return mid;
        }


        if(arr[mid] > target){
            return bisectRight(arr, target, left, mid - 1);
        }else{
            return bisectRight(arr, target, mid + 1, right);
        }

    }


    public static int count(int[] arr, int target){
        int left = findLeftMost(arr, target);

        if(left == -1){
            return 0;
        }

        int right = findRightMost(arr,target);
        return right - left + 1;
    }

}
