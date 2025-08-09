import time
from typing import List, Optional, Tuple

class SudokuSolver:
    def __init__(self):
        self.board = None
        self.solutions = []
        self.max_solutions = 1  # Limit to find only one solution by default
    
    def load_board(self, board: List[List[int]]) -> bool:
        """
        Load a Sudoku board and validate it.
        
        Args:
            board: 2D list representing the Sudoku board
            
        Returns:
            bool: True if board is valid, False otherwise
        """
        if not self._is_valid_board(board):
            return False
        
        self.board = [row[:] for row in board]  # Create a copy
        return True
    
    def _is_valid_board(self, board: List[List[int]]) -> bool:
        """Check if the board is a valid Sudoku board."""
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False
        
        # Check for invalid numbers
        for row in board:
            for cell in row:
                if not isinstance(cell, int) or cell < 0 or cell > 9:
                    return False
        
        # Check for conflicts in initial board
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    if not self._is_valid_placement(board, i, j, board[i][j]):
                        return False
        
        return True
    
    def _is_valid_placement(self, board: List[List[int]], row: int, col: int, num: int) -> bool:
        """Check if placing 'num' at position (row, col) is valid."""
        # Check row
        for x in range(9):
            if x != col and board[row][x] == num:
                return False
        
        # Check column
        for x in range(9):
            if x != row and board[x][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if (start_row + i != row or start_col + j != col) and \
                   board[start_row + i][start_col + j] == num:
                    return False
        
        return True
    
    def _find_empty(self, board: List[List[int]]) -> Optional[Tuple[int, int]]:
        """Find an empty cell (represented by 0)."""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None
    
    def _get_candidates(self, board: List[List[int]], row: int, col: int) -> List[int]:
        """Get all valid candidates for a cell."""
        candidates = []
        for num in range(1, 10):
            if self._is_valid_placement(board, row, col, num):
                candidates.append(num)
        return candidates
    
    def solve(self, find_all: bool = False) -> bool:
        """
        Solve the Sudoku puzzle.
        
        Args:
            find_all: If True, find all possible solutions
            
        Returns:
            bool: True if at least one solution found
        """
        if self.board is None:
            return False
        
        self.solutions = []
        self.max_solutions = float('inf') if find_all else 1
        
        return self._solve_recursive([row[:] for row in self.board])
    
    def _solve_recursive(self, board: List[List[int]]) -> bool:
        """Recursive function to solve the Sudoku."""
        empty = self._find_empty(board)
        if not empty:
            self.solutions.append([row[:] for row in board])
            return len(self.solutions) >= self.max_solutions
        
        row, col = empty
        
        # Get candidates for this cell
        candidates = self._get_candidates(board, row, col)
        
        # Try each candidate
        for num in candidates:
            board[row][col] = num
            
            if self._solve_recursive(board):
                return True
            
            board[row][col] = 0  # Backtrack
        
        return False
    
    def get_solution(self) -> Optional[List[List[int]]]:
        """Get the first solution found."""
        return self.solutions[0] if self.solutions else None
    
    def get_all_solutions(self) -> List[List[List[int]]]:
        """Get all solutions found."""
        return self.solutions
    
    def print_board(self, board: Optional[List[List[int]]] = None) -> None:
        """Print the Sudoku board in a readable format."""
        if board is None:
            board = self.board
        
        if board is None:
            print("No board loaded!")
            return
        
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                
                if j == 8:
                    print(board[i][j] if board[i][j] != 0 else ".")
                else:
                    print(str(board[i][j]) + " " if board[i][j] != 0 else ". ", end="")
    
    def get_difficulty_estimate(self) -> str:
        """Estimate the difficulty of the puzzle based on empty cells."""
        if self.board is None:
            return "No board loaded"
        
        empty_cells = sum(1 for row in self.board for cell in row if cell == 0)
        
        if empty_cells <= 20:
            return "Easy"
        elif empty_cells <= 40:
            return "Medium"
        elif empty_cells <= 60:
            return "Hard"
        else:
            return "Expert"


def solve_sudoku_advanced(board: List[List[int]], find_all: bool = False) -> List[List[List[int]]]:
    """
    Advanced Sudoku solver function.
    
    Args:
        board: 2D list representing the Sudoku board
        find_all: If True, find all possible solutions
        
    Returns:
        List of solutions (each solution is a 2D list)
    """
    solver = SudokuSolver()
    if solver.load_board(board):
        solver.solve(find_all)
        return solver.get_all_solutions()
    return []


# Example usage and testing
if __name__ == "__main__":
    # Test puzzle
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
    
    print("=== Advanced Sudoku Solver ===\n")
    
    # Create solver instance
    solver = SudokuSolver()
    
    # Load and analyze puzzle
    if solver.load_board(puzzle):
        print("Original puzzle:")
        solver.print_board()
        print(f"\nDifficulty: {solver.get_difficulty_estimate()}")
        print(f"Empty cells: {sum(1 for row in puzzle for cell in row if cell == 0)}")
        
        # Solve puzzle
        print("\n" + "="*50)
        start_time = time.time()
        
        if solver.solve():
            end_time = time.time()
            solution = solver.get_solution()
            
            print(f"Solution found in {end_time - start_time:.4f} seconds!")
            print("\nSolved puzzle:")
            solver.print_board(solution)
            
            # Verify solution
            print("\nVerifying solution...")
            if solver.load_board(solution):
                print("✓ Solution is valid!")
            else:
                print("✗ Solution is invalid!")
        else:
            print("No solution found!")
    else:
        print("Invalid puzzle!")
    
    # Test with multiple solutions puzzle
    print("\n" + "="*50)
    print("Testing with puzzle that has multiple solutions...")
    
    multi_solution_puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    solutions = solve_sudoku_advanced(multi_solution_puzzle, find_all=True)
    print(f"Found {len(solutions)} solutions for empty puzzle")
    if solutions:
        print("First solution:")
        solver.print_board(solutions[0]) 