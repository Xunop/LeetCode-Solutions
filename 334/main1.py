class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        # `first` represents the smallest number,
        # `sec` represents the second smallest number
        first = sec = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= sec:
                sec = num
            # If current number > first and > sec
            # True
            else:
                return True
        return False
