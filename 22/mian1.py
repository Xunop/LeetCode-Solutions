class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, sub_str):
            if left == 0 and right == 0:
                res.append(sub_str)
                return
            
            if left > 0:
                dfs(left - 1, right, sub_str + '(')
            if right > left:
                dfs(left, right - 1, sub_str + ')')
        
        dfs(n, n, "")
        return res
