#!/usr/bin/env python3
""" doc doc doc """
import sys


def is_safe(board, row, col):
    """doc doc doc"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1,)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col, solutions):
    """doc doc doc"""
    if col >= len(board):
        solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, solutions) or res
            board[i][col] = 0
    return res


def nquuens(N):
    """doc doc doc"""
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage nqueens N")
        sys.exit(1)
        
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nquuens(N)
