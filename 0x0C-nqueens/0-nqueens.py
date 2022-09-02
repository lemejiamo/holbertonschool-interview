#!/usr/bin/python3
""" Program that solves the N queens problem."""

import sys


def Main_queens():
    """
    Entry point

    Attributtes:
     *answer: List that contains a solution
     *numberOfSolutions: number of possible solutions to the puzzle

    """

    try:
        nQueens = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if nQueens < 4:
        print("N must be at least 4")
        exit(1)

    table = [-1 for pos in range(0, nQueens)]
    Solution(table, 0, nQueens)


def Solution(table, column, nQueens):
    if(column == nQueens):
        print(table)
        return 1

    else:
        for table[column] in range(0, nQueens):  # itera sobre las filas
            if(Row_Validation(table, column) and Diagonal_Validation(table, column)):
                Solution(table, column + 1, nQueens)



def Row_Validation(table, column):
    for pos in range(len(table)):
        if pos == column:
            pass
        else:
            if table[pos] == table[column]:
                return False
        return True


def Diagonal_Validation(table, column):
    for pos in range(0, column):
        if pos == column:
            pass
        else:
            subsColumns = pos - column
            subsRows = table[pos] - table[column]
            # print("subr {}, sub column {}".format(subsRows,subsColumns))
            if (subsColumns - subsRows == 0) or (subsColumns + subsRows == 0):
                return False
    return True

if __name__ == "__main__":

    Main_queens()
