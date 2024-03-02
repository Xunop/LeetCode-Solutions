class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def b_search(arr, target):
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return arr[left] == target
        for arr in matrix:
            if b_search(arr, target):
                return True
        return False
