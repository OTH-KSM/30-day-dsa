You're given an array nums and a value val. Implement an in-place algorithm to remove all instances of val and return the new length k. Elements beyond k don’t matter. The solution should not use extra space.

## Data Structure:
I use the input list nums directly and a pointer variable k to track the next valid index.
## Strategy:
This is an in-place overwrite problem.
As I loop through the array, I overwrite the values that should stay (i.e., not equal to val) at the front of the array, keeping track of where to place them using index k.
## Steps to Solve:

I initialize a pointer k = 0, which tracks the index of the next element to keep.

I loop through each element in nums.

If the current value is not equal to val, I copy it to nums[k] and increment k.

After the loop ends, I return k as the number of elements that are not equal to val.

## Time Complexity: O(n)
I visit each element once in a single pass through the array.

## Space Complexity: O(1)
I don’t use any additional space — the operation is done in-place.

## 🔗 Code Link:       NeetCode link for Remove Element.