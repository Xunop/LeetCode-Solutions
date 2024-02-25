class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, num in enumerate(nums):
            if target - num in res:
                return [res[target - num], i]
            else:
                res[num] = i
        return res
