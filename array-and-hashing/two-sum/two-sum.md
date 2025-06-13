Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.
Explain your thought process, the data structure you used, and how your approach works

## Data Structure:
I use a hashmap (dictionary) to store each number in the array along with its index.
## Strategy:
I want to find two numbers a and b such that a + b = target.
To do this efficiently, I store all numbers with their indices in a hashmap, then look up target - current_value while iterating.

## Why a Hashmap?
A hashmap gives me constant-time (O(1)) lookups.
I use it to check if the complement (target - n) exists.
This avoids a nested loop and reduces time complexity to linear.

## Steps to Solve:


Create an empty dictionary numsMap to store number: index.

Loop once through the array and map each number to its index.

Loop again through the array:

For each number n, compute the difference target - n.

Check if that difference exists in numsMap and that it’s not the same index.

If found, return [i, numsMap[diff]].

## Time Complexity:
O(n) — I loop through the array twice (2n), and all dictionary operations are O(1).

## Space Complexity:
O(n) — I store up to n entries in the hashmap for the array values and their indices.

## Code Link:
🔗 https://neetcode.io/problems/two-sum?list=neetcode250