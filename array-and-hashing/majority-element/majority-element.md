You’re given an array of integers nums, where it is guaranteed that a majority element exists — an element that appears more than ⌊n / 2⌋ times.

Can you find it in O(n) time and O(1) space?

## Data Structure:
I use two variables:

number to store the current candidate for the majority.

seen as a count or vote balance.

## Strategy (Boyer-Moore Majority Vote Algorithm):
I treat every occurrence of the majority element as a vote +1, and every other number as a vote -1.

If my vote count seen drops to 0, I reset the candidate to the current number and start counting again.

Since the majority element appears more than half the time, it will always survive this voting system and end up as the final candidate.

## Steps to Solve:

I initialize number to nums[0] and seen to 1.

I iterate from index 1 to the end of the array:

If nums[i] is equal to number, I increment seen.

Otherwise, I decrement seen.

If seen becomes 0:

I update number to the current nums[i].

I reset seen to 1.

After finishing the loop, I return number.

## Time Complexity: O(n)
I make a single pass through the array.

## Space Complexity: O(1)
I only use two variables regardless of input size.

## Code Link:
🔗 https://neetcode.io/problems/majority-element?list=neetcode250