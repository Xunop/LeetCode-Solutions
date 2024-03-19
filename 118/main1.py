class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            # Initialize the list with 1
            res.append([1]*(i + 1))
            # Start traversing from the second element to the penultimate element 
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res
