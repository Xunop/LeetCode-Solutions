class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if len(candidates) == 0:
            return res
        def dfs(path, sum, dep):
            if sum > target:
                return
            elif sum == target:
                res.append(path)
            for i in range(dep, len(candidates)):
                sum += candidates[i]
                dfs(path + [candidates[i]], sum, i)
                sum -= candidates[i]
        dfs([], 0, 0)
        return res
