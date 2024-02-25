class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = 0
        length = len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                zero_cnt += 1
            else:
                nums[i - zero_cnt] = nums[i]
        for i in range(zero_cnt):
            nums[length - 1 - i] = 0
