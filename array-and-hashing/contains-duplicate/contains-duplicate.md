You’re given an integer array nums. Your task is to determine if any value appears at least twice.
Can you solve this in linear time while minimizing space usage?

## Data Structure:
I use a set to keep track of the numbers I've seen as I iterate.

## Strategy:
As I go through each number, I check if it already exists in the set.

If it does, that means I found a duplicate — I return True.

If not, I add it to the set.
If I finish the loop without finding any duplicates, I return False.

## Why a Set Instead of Other Structures?

Sets allow for O(1) average time complexity for both lookups and inserts.

A list would require O(n) lookups — inefficient.

A dict could work, but I don’t need to store frequencies — I only care about presence.

## Steps to Solve:

I initialize an empty set called seen.

I loop through each number in the input array nums.

If the number is already in seen, I return True.

Otherwise, I add the number to the set.

If I finish the loop, I return False.

## Time Complexity: O(n)
I traverse the array once, and each lookup/insert in the set is O(1) on average.

## Space Complexity: O(n)
In the worst case (no duplicates), I store all n elements in the set.


## Code Link:
🔗 https://neetcode.io/problems/duplicate-integer?list=neetcode250