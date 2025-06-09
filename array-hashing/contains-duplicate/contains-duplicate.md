You are given an integer array nums. Write a function to determine if the array contains any duplicates.
Return True if any value appears at least twice in the array, and False if every element is distinct.

## Data Structure:
set — to track seen elements efficiently with O(1) average lookup.

## Strategy:
Iterate through each element in the array and check if it’s already in the seen set.
If yes, return True immediately (duplicate found).
If no, add the element to seen.
If iteration completes without duplicates, return False.

## Why this structure?
Sets provide constant-time membership checks, making duplicate detection efficient and clean.

## Steps to Solve:

Initialize an empty set seen.

Loop over each number n in nums:

If n in seen, return True.

Else, add n to seen.

If loop finishes, return False.

## Time Complexity:
O(n) — each element is checked once, and set operations are O(1) average.

## Space Complexity:
O(n) — worst case all elements are unique, stored in the set.