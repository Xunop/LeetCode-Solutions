# 1. Greedy
# 2. Keep track of the maximum reach
# 3. Update the next jump in the current jump
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        jumps = 0
        max_reach = 0
        end = 0
        for i in range(n - 1):
            # Get the maximum reach
            max_reach = max(max_reach, i + nums[i])
            # Update next jump in current jump
            if i == end:
                jumps += 1
                # Reached the end
                end = max_reach
        return jumps
