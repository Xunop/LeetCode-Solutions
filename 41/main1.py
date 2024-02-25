class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1, 2 ** 31 - 1):
            if i not in nums:
                return i
