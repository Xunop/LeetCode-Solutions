# Time limit exceeded
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def dfs(nums, idx):
            if idx == len(nums) - 1:
                return 0
            for i in range(idx + 1, len(nums)):
                if nums[i] > nums[idx]:
                    return i - idx
            return 0
        ans = []
        for i in range(len(temperatures)):
            ans.append(dfs(temperatures, i))
        return ans
