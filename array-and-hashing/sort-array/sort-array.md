You're given an unsorted array of integers nums.
Your task is to sort the array in ascending order using a sorting algorithm with O(n log n) time complexity.
You cannot use built-in sorting functions.

How would you solve this?

## Data Structure:
I use recursive function calls and temporary subarrays (larr, rarr) to implement Merge Sort.

## Strategy:
Use the divide-and-conquer strategy of merge sort:

Divide the array into two halves until each piece has one element.

Merge the two sorted halves back together in a sorted way.

## Why Merge Sort?

It's a stable and reliable sorting algorithm.

It guarantees O(n log n) time complexity.

Suitable when you want to avoid worst-case O(n²) of quicksort.

## Steps to Solve:

Define a mergeSort function that divides the array into halves.

Recursively sort the left and right halves.

Use a helper merge function to merge two sorted subarrays into one.

The merge function:

Creates temporary arrays for left and right halves.

Compares and places elements back in the correct position in the main array.

## Time Complexity: O(n log n)
Because we divide the array in half log(n) times and process all n elements at each level.

## Space Complexity: O(n)
Due to the extra space used for temporary subarrays during merging.

