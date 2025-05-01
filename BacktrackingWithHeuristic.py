import time

steps = 0  # Counter for the number of attempts

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def get_possible_values(board, row, col):
    if board[row][col] != 0:
        return []

    possible = set(range(1, 10))
    # Remove from row
    possible -= set(board[row])
    # Remove from column
    possible -= {board[i][col] for i in range(9)}
    # Remove from 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            possible.discard(board[box_row + i][box_col + j])
    return list(possible)

def find_mrv_cell(board):
    min_options = 10
    best_cell = None
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                options = get_possible_values(board, row, col)
                if len(options) < min_options:
                    min_options = len(options)
                    best_cell = (row, col, options)
                if min_options == 1:  # can't get better than this
                    return best_cell
    return best_cell

def solve_sudoku_mrv(board):
    global steps
    cell = find_mrv_cell(board)
    if not cell:
        return True  # Solved
    row, col, options = cell
    for num in options:
        steps += 1
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku_mrv(board):
                return True
            board[row][col] = 0
    return False

def read_board_from_file(filename):
    board = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            board.append(row)
    return board

# Use raw string or / in path
sudoku_board = read_board_from_file(r"C:\Users\Ahmad Mnadili\Downloads\sudoku.txt")

start_time = time.time()

if solve_sudoku_mrv(sudoku_board):
    end_time = time.time()
    print("Solved board (using MRV heuristic):")
    print_board(sudoku_board)
    print(f"\nNumber of attempts: {steps}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
else:
    print("No solution exists.")
