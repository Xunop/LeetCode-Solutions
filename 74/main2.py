class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_col(arr, target):
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

        def search_row(arr, target):
            up, down = 0, len(arr)
            if arr[up] < target:
                return -1
            while up < down:
                mid = (up + down) // 2
                if arr[mid] > target:
                    down = mid
                else:
                    up = mid + 1
            return up

        row = search_row([matrix[i][0] for i in range(len(matrix))], target)
        print(row)

        if row < 0 or row >= len(matrix):
            return False
        return search_col(matrix[row], target)
