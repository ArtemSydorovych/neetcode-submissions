class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or word[i] != board[r][c]):
                return False
            

            board[r][c] = '#'
            res = False
            for dr, dc in dirs:
                res = res or dfs(dr +r, dc + c, i + 1)
            
            board[r][c] = word[i]
            return res
    

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False
