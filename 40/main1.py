class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time limit
        res = []
        def dfs(start, path, sum):
            if sum > target:
                return
            elif sum == target:
                path = sorted(path)
                if path not in res:
                    res.append(path)
                return
            for i in range(start, len(candidates)):
                dfs(i + 1, path + [candidates[i]], sum + candidates[i])
        dfs(0, [], 0) 
        return res
