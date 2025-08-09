def solve_sudoku(board):
    """
    Solve a Sudoku puzzle using backtracking algorithm.
    
    Args:
        board: 2D list representing the Sudoku board (0 represents empty cells)
    
    Returns:
        bool: True if solution found, False otherwise
    """
    def is_valid(board, row, col, num):
        """Check if placing 'num' at position (row, col) is valid."""
        # Check row
        for x in range(9):
            if board[row][x] == num:
                return False
        
        # Check column
        for x in range(9):
            if board[x][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        
        return True
    
    def find_empty(board):
        """Find an empty cell (represented by 0)."""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None
    
    def solve(board):
        """Recursive function to solve the Sudoku."""
        empty = find_empty(board)
        if not empty:
            return True  # Puzzle is solved
        
        row, col = empty
        
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                
                if solve(board):
                    return True
                
                board[row][col] = 0  # Backtrack
        
        return False
    
    return solve(board)

def print_board(board):
    """Print the Sudoku board in a readable format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Example usage
if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Original Sudoku puzzle:")
    print_board(puzzle)
    print("\n" + "="*50 + "\n")
    
    if solve_sudoku(puzzle):
        print("Solved Sudoku puzzle:")
        print_board(puzzle)
    else:
        print("No solution exists!") 