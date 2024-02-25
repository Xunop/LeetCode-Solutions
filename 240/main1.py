class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        for num in matrix:
            if num[0] <= target <= num[-1]:
                if res:
                    return True
                res = target in num
        return False
