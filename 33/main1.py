class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # The left part is sorted
            elif nums[mid] < nums[right]:
                # If the target is in the left part
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                # If the target is in the right part
                else:
                    right = mid - 1
            # The right part is sorted
            elif nums[mid] >= nums[right]:
                # If the target is in the right part
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                # If the target is in the left part
                else:
                    left = mid + 1
        return left if nums[left] == target else -1
