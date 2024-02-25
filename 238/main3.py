class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix, suffix = 1, 1
        for i in range(len(nums)):
            res[i] *= prefix
            res[len(nums) - i - 1] *= suffix
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
        return res
