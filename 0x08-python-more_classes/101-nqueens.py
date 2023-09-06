import sys

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

        for j in range(n):
            if board[i][j] == 1 and (abs(row - i) == abs(col - j)):
                return False

    return True

def print_solution(board):
    for row in board:
        print(row)

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        for row in solution:
            print_solution(row)
        print()

def solve_nqueens_util(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
