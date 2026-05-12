class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1) No duplicates in ROWS
        rows = collections.defaultdict(set)

        # 2) No duplicates in COLUMNS
        cols = collections.defaultdict(set)

        # 3) No duplicates in 3x3 GRIDS
        grid_block = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in grid_block[(row // 3, col // 3)]):
                    return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                grid_block[((row // 3, col // 3))].add(board[row][col])
        return True
