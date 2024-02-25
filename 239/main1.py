class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left, idx = 0, len(nums) - 1
        while (idx < len(nums)):
            res.append(max(nums[left:idx]))
            left += 1
            idx += 1
        return res
