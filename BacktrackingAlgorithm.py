
import time
steps = 0  # Counter for the number of attempts
def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
def is_valid(board, row, col, num):
    if num in board[row]:  # Row check
        return False
    if num in [board[i][col] for i in range(9)]:  # Column check
        return False
    # 3x3 box check
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True
def solve_sudoku(board):
    global steps
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):
                    steps += 1
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True
def read_board_from_file(filename):
    board = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            board.append(row)
    return board

# Read board from file
sudoku_board = read_board_from_file("sudoku.txt")
start_time = time.time()
if solve_sudoku(sudoku_board):
    end_time = time.time()
    print("Solved board:")
    print_board(sudoku_board)
    print(f"\nNumber of attempts: {steps}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
else:
    print("No solution exists.")
