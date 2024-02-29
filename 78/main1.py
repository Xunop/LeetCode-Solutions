class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(x, tmp):
            res.append(tmp)
            for i in range(x, len(nums)):
                dfs(i + 1, tmp + [nums[i]])
        dfs(0, [])
        return res
