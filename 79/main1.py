class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, board, sub_str):
            if len(sub_str) == 0:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != sub_str[0]:
                return False
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, board, sub_str[1:]) or dfs(i - 1, j, board, sub_str[1:]) or dfs(i, j + 1, board, sub_str[1:]) or dfs(i, j - 1, board, sub_str[1:])
            board[i][j] = tmp
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, board, word):
                        return True
        return False
