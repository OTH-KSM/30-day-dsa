from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, M, R):
            larr = arr[L: M+1]
            rarr = arr[M+1: R+1]
            left = 0
            right = 0
            K = L
            while left < len(larr) and right < len(rarr):
                if larr[left] <= rarr[right]:
                    arr[K] = larr[left]
                    left += 1
                else:
                    arr[K] = rarr[right]
                    right += 1
                K += 1
            while left < len(larr):
                arr[K] = larr[left]
                left += 1
                K += 1
            while right < len(rarr):
                arr[K] = rarr[right]
                right += 1
                K += 1

        def mergeSort(arr, l, r):
            if l == r:
                return
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return

        mergeSort(nums, 0, len(nums) - 1)
        return nums