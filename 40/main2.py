class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start, path, sum):
            if sum > target:
                return
            elif sum == target:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, path + [candidates[i]], sum + candidates[i])
        dfs(0, [], 0)
        return res
