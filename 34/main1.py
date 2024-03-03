class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        def get_idx(nums, target):
            if len(nums) == 0:
                return -1
            left, right = 0, len(nums) - 1
            if nums[0] > target:
                return -1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left if nums[left] == target else -1

        idx = get_idx(nums, target)
        if idx == -1:
            return [-1, -1]
        left, right = idx, idx
        while left > 0 and nums[left - 1] == target:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] == target:
            right += 1
        return [left, right]
