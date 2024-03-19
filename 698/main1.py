class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if (not sum(nums) % k):
            return False
        nums.sort(reverse=True)
        target = sum(nums) // k
        n = len(nums)
        vis = [0] * n
        # dfs: index: 当前考虑的数字下标, cur: 当前子集的和, cnt: 当前已经分成的子集数, vis: 记录当前数字是否被使用
        # dfs 函数的定义为: 从 index 开始，是否能够找到 k 个和为 target 的子集

        def dfs(index, cur, cnt, vis):
            if cnt == k:
                return True
            if cur == target:
                return dfs(n - 1, 0, cnt + 1, vis)
            for i in range(index, -1, -1):
                if vis[i] or cur + nums[i] > target:
                    continue
                vis[i] = 1
                # 如果找到了一个合适的子集，直接返回 True
                if dfs(i - 1, cur + nums[i], cnt, vis):
                    return True
                vis[i] = 0
                # 在 if dfs(i - 1, cur + nums[i], cnt, vis) 这一步中，已经对所有包含 nums[i] 的子集进行了搜索，但是没有找到合适的子集，所以说明 nums[i] 无法放入任何一个子集，所以直接返回 False
                # 可以使用示例 [3, 4, 4, 9] k = 2 进行调试
                if cur == 0:
                    return False
            return False
        return dfs(n - 1, 0, 0, vis)
