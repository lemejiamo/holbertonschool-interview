#!/usr/bin/env/ python3
"""
    Script to rotate a matrix
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """method to rotate a 2d matrix in a 90 degrees"""
    if matrix is None:
        return None

    # informacion inicial de la matrix
    matrixLength = len(matrix)
    # avance inical
    jump = matrixLength - 1

    for _row in range(matrixLength - 1):
        _column = _row

        while _column < (jump + _row):
            origin = [_row, _column]
            current = []
            rowFactor = origin[1] - origin[0]
            columnFactor = jump - rowFactor
            temp = None
            counter = 0

            while current != origin:
                # set initial position
                if current == []:
                    current = list.copy(origin)

                # set the number to switch
                if temp is None:
                    numberToSwitch = matrix[current[0]][current[1]]
                else:
                    numberToSwitch = temp

                # set the destiny
                rowDestiny = current[1]
                if counter == 0 or counter == 3:
                    columnDestiny = current[1] + columnFactor
                else:
                    columnDestiny = current[1] - columnFactor

                counter = counter + 1

                # storing the number  of the destiny in a tmp
                temp = matrix[rowDestiny][columnDestiny]

                # swithcing number
                matrix[rowDestiny][columnDestiny] = numberToSwitch

                # set new origin for the next iteration
                current[0], current[1] = rowDestiny, columnDestiny
                # set new factors
                columnFactor, rowFactor = rowFactor, columnFactor

            _column = _column + 1

        jump = jump - 2
        if jump < 1:
            break
