Given two strings s and t, return True if t is an anagram of s, and False otherwise.
Explain your approach, the data structure you chose, and walk me through your reasoning and code

## Data Structure:
I use a fixed-size list of 26 integers to count character frequencies for lowercase letters.

## Strategy:
I first check if the lengths of the two strings differ.
If they do, they can’t be anagrams.
If the lengths match, I create an array to count each character in s and subtract each character in t.
If all counts are zero, the strings are anagrams.

## Why a List Instead of a Dict?

The input is limited to lowercase English letters.

A list of size 26 is more space-efficient and faster than a hashmap.

Access and update operations are constant time.

## Steps to Solve:

If len(s) != len(t), return False.

Initialize a count array of size 26 filled with zeroes.

Loop through both strings:

Increment count at the index for the character in s.

Decrement count at the index for the character in t.

At the end, check if all elements in the count array are 0.

If so, return True; otherwise, return False.

## Time Complexity: O(n)
I loop through the strings once (n is the length of s and t), and array operations are O(1).

## Space Complexity: O(1)
The count array has a fixed size of 26, regardless of input size.

## Code Link:
🔗 https://neetcode.io/problems/valid-anagram?list=neetcode250