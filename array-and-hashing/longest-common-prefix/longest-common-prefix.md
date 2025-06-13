You’re given an array of strings, and you're asked:
"Write an efficient function to find the longest common prefix shared among all the strings."

How would you solve this while maintaining efficiency and clean logic?

## Data Structure:
I use a string (prefix) to represent the current assumed longest common prefix.
## Strategy:
I start by assuming the entire first string is the longest common prefix.
Then I iterate over the remaining strings and shrink the prefix from the end until it matches the beginning of each string.
This pattern is called “Shrink Until Valid” — it’s powerful when solving problems that ask for shared features or constraints across multiple elements.
## Steps to Solve:

Set prefix to the first string in the list.

Loop through each of the remaining strings.

While the current string doesn’t start with prefix, reduce the length of prefix from the end by one character.

If prefix becomes empty, return an empty string.

After the loop, return the final value of prefix.

## Time Complexity: O(n × m)
Where n is the number of strings and m is the average length of the strings.
In the worst case, we may need to compare every character of every string with the prefix.

## Space Complexity: O(1)
We only use a few variables regardless of input size.

## Code Link:
🔗 Longest Common Prefix – NeetCode