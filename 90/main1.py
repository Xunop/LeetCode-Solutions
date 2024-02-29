class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        def dfs(start, tmp):
            if tmp in res:
                return
            res.append(tmp)
            for i in range(start, len(nums)):
                dfs(i + 1, tmp + [nums[i]])
        dfs(0, [])
        return res
