Given a list of strings, return groups of anagrams together. You should aim for the most time-efficient solution. How would you do it?

🧠 Data Structure:
I use a hashmap (defaultdict(list)) to group strings by their anagram signature — a fixed-size list of 26 integers representing character frequencies.

🔍 Strategy:
Anagrams share the same character counts.
So instead of sorting each string (which takes O(m log m)), I track how many times each letter appears using a 26-element list (since all characters are lowercase English letters).
I convert that list into a tuple to use as a dictionary key (lists can’t be keys because they’re mutable).

🪜 Steps to Solve:

I initialize an empty hashmap where each key is a 26-character tuple and each value is a list of strings (anagram group).

For each string s in the input:

I initialize a list of 26 zeros.

I loop through each character c in s, and increment its corresponding index.

I convert the list to a tuple and use it as the key in the hashmap.

I append the string to the corresponding group.

I return all the hashmap’s values as the grouped anagrams.

⏱️ Time Complexity: O(n * m)

n is the number of strings, m is the average string length.

For each string, I loop through its characters (O(m)) and update a 26-element list.

🧠 Space Complexity: O(n * m)

I store all strings in the hashmap (grouped), and each key is a 26-size tuple — still constant space per key.



##  Why This Approach?

No sorting: Avoids the O(m log m) cost per string.

Fixed structure: Character count list is always size 26, so operations are effectively constant time.

Hashmap + Tuple: Clean grouping mechanism with excellent average-case performance.

## 🔗 Code Link:
https://neetcode.io/problems/anagram-groups?list=neetcode250