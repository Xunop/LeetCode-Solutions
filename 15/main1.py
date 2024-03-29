class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            # skip duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                tSum = nums[i] + nums[l] + nums[r]
                if tSum == 0:
                    tmp = [nums[i], nums[l], nums[r]]
                    res.append(tmp)
                    while (l < r and nums[l] == nums[l + 1]):
                        l += 1
                    while (l < r and nums[r] == nums[r - 1]):
                        r -= 1
                    l += 1
                    r -= 1
                elif tSum < 0:
                    l += 1
                else:
                    r -= 1
        return res
