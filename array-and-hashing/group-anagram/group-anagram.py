from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagDict = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            anagDict[tuple(letters)].append(s)
        return anagDict.values()