#!/usr/bin/python3
""" Script to solve N queens problem
"""

import sys


def is_safe(board, row, col, n):
    """Checks that a (row, col) of board is safe to place queen"""
    for i in range(row):
        if (board[i] == col or board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def nqueens(n):
    """Generate all solutions"""
    def backtrack(row, board):
        if row == n:
            print_solution(board, n)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1, board)

    board = [-1] * n
    backtrack(0, board)


def print_solution(board, n):
    """Print board as list of [row, col] pairs"""
    solution = [[r, board[r]] for r in range(n)]
    print(solution)


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)


if __name__ == "__main__":
    main()
