from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        pref_length = len(strs[0])
        for s in strs[1:]:
            while prefix[:pref_length] != s[:pref_length]:
                pref_length -= 1
        return prefix[:pref_length]