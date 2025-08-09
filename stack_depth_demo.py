import sys
import inspect

def get_stack_depth():
    """Get current stack depth."""
    return len(inspect.stack())

def solve_sudoku_with_depth_tracking(board):
    """
    Solve Sudoku with stack depth tracking.
    """
    def is_valid(board, row, col, num):
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
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None
    
    def solve(board, depth=0):
        """Recursive function with depth tracking."""
        current_depth = get_stack_depth()
        empty_cells = sum(1 for row in board for cell in row if cell == 0)
        
        print(f"Depth: {depth}, Stack frames: {current_depth}, Empty cells: {empty_cells}")
        
        empty = find_empty(board)
        if not empty:
            print(f"✓ SOLVED at depth {depth}!")
            return True
        
        row, col = empty
        
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                print(f"  Trying {num} at ({row},{col}) - depth {depth}")
                
                if solve(board, depth + 1):
                    return True
                
                board[row][col] = 0
                print(f"  Backtracking from ({row},{col}) - depth {depth}")
        
        return False
    
    return solve(board)

def print_board(board):
    """Print the Sudoku board."""
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

if __name__ == "__main__":
    # Simple puzzle for demonstration
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
    
    print("Original puzzle:")
    print_board(puzzle)
    print(f"\nInitial stack depth: {get_stack_depth()}")
    print("\n" + "="*60)
    print("SOLVING WITH DEPTH TRACKING:")
    print("="*60)
    
    if solve_sudoku_with_depth_tracking(puzzle):
        print("\n" + "="*60)
        print("FINAL SOLUTION:")
        print_board(puzzle)
    else:
        print("No solution found!")
    
    print(f"\nFinal stack depth: {get_stack_depth()}") 
 