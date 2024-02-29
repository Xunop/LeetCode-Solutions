class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(x):
            if x == len(nums) - 1:
                res.append(list(nums))
                return
            # Store the used numbers in a list
            used = []
            for i in range(x, len(nums)):
                if nums[i] in used:
                    continue
                used.append(nums[i])
                # Only swap the numbers that are not used in current for loop
                nums[i], nums[x] = nums[x], nums[i]
                backtracking(x + 1)
                nums[i], nums[x] = nums[x], nums[i]
        backtracking(0)
        return res
