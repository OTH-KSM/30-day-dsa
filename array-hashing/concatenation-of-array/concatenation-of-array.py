from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        s = [0] * length * 2
        for i in nums:
            s[i] = s[i + length] = nums[i]
        return s