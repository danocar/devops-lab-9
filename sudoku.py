def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def solve_sudoku(board):
    import copy

    # Input validation BEFORE solve() is called
    if not isinstance(board, list) or len(board) != 9:
        raise TypeError("Input must be a 9x9 2D list of integers.")

    for row in board:
        if not isinstance(row, list) or len(row) != 9:
            raise TypeError("Each row must be a list of 9 integers.")
        for cell in row:
            if not isinstance(cell, int):
                raise TypeError("Each cell must be an integer.")

    board_copy = copy.deepcopy(board)
    if solve(board_copy):
        return board_copy
    else:
        return None


if __name__ == "__main__":
    test_board = [
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

    result = solve_sudoku(test_board)

    if result:
        for row in result:
            print(row)
    else:
        print("No solution found.")




