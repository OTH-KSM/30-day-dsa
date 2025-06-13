Given an array of integers nums, return a new array that's the concatenation of nums with itself.
What data structure would you use? What’s your strategy, time/space complexity, and can you implement it?

## Data Structure:
I use a pre-allocated list of size 2n to store the result.

## Strategy:
This is an array manipulation problem.
Instead of looping through nums twice, I use a single loop and write each element in two positions at once.

## Why This Strategy Works:
We only loop once over the array and fill both the original and duplicated values in one pass.
This reduces overhead and ensures both time and space remain linear.

## Steps to Solve:

I calculate the length of the input array nums.

I initialize a new array newArr of size 2 * length.

I loop through the original array once:

At each index i, I set both newArr[i] and newArr[i + length] to nums[i].

I return newArr as the result.


## Time Complexity: O(n)
I loop through nums once, and every write is done in constant time.

## Space Complexity: O(n)
I allocate a new array of size 2n.

## Code Link:
🔗 https://neetcode.io/problems/concatenation-of-array?list=neetcode250