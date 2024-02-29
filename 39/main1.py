class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(path, sum):
            if sum == target:
                path = sorted(path)
                if path not in res:
                    res.append(path)
                return
            elif sum > target:
                return

            for num in candidates:
                sum += num
                dfs(path + [num], sum)
                sum -= num
        dfs([], 0)
        return res
