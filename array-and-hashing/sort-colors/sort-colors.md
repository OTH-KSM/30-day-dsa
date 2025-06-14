You're given an array nums with values 0, 1, and 2, representing the colors red, white, and blue.
You must sort the array in-place so that all 0s come first, followed by 1s, then 2s.
Do not use a library sort function.

How would you solve this efficiently in one pass?

## Data Structure:
The array is modified in-place using three pointers: left, mid, and right.

## Strategy: Dutch National Flag Algorithm
Use three pointers to partition the array into three sections:

Elements before left are all 0s.

Elements between left and mid are all 1s.

Elements after right are all 2s.

Move elements accordingly as you iterate.

## Why This Approach?

Efficient one-pass sorting.

Operates in-place.

Avoids extra space or multiple passes.

## Steps to Solve:

Initialize:

left at index 0 (next position to place 0),

mid at index 0 (current element being evaluated),

right at the end of the array (next position to place 2).

Iterate while mid <= right:

If nums[mid] == 0:
Swap with nums[left], move both left and mid forward.

If nums[mid] == 1:
Move mid forward.

If nums[mid] == 2:
Swap with nums[right], move right backward, but don't move mid (recheck swapped value).

## Time Complexity:
O(n)
Each element is visited at most once.

## Space Complexity:
O(1)
Sorting is done in-place with constant extra space.

## Code Link:
🔗 https://neetcode.io/problems/sort-colors?list=neetcode250