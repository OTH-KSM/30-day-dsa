Given an array of integers nums, return a new array that's the concatenation of nums with itself.
What data structure would you use? What’s your strategy, time/space complexity, and can you implement it?

## Data Structure:
I use a list to build the final result — ans = [].

## Strategy:
This is a basic array manipulation problem.
I loop through the input array twice, appending each element to a new array.

## Steps to Solve:

I initialize an empty result array ans.

I loop 2 times.

In each pass, I go through every element in nums and append it to ans.

I return the final result.

## Time Complexity: O(n)
Even though I loop through the array twice, it’s still linear — 2n is treated as O(n).


## Space Complexity: O(n)
I create a new array of size 2n, which is proportional to the input size.

## Code Link:
🔗 https://neetcode.io/problems/concatenation-of-array?list=neetcode250