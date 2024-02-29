class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(x):
            if x == len(nums) - 1:
                res.append(list(nums))
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                backtracking(x + 1)
                nums[i], nums[x] = nums[x], nums[i]
        backtracking(0)
        return [list(x) for x in set(tuple(x) for x in res)]
