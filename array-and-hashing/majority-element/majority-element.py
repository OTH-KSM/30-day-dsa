from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number = nums[0]
        seen = 1
        for i in range(1, len(nums)):
            if nums[i] != number:
                seen -= 1
            else:
                seen += 1
            if seen == 0:
                number = nums[i]
                seen += 1
        return number