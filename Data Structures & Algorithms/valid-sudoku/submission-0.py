class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        # rows
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if col == '.':
                    continue
                
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(col)
                cols[c].add(col)
                squares[(r // 3, c // 3)].add(col)
        
        return True
        