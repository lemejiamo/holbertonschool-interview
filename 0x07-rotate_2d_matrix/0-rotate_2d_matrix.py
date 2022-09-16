#!/usr/bin/env/ python3
"""
    Script to rotate a matrix
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """method to rotate a 2d matrix in a 90 degrees"""
    if matrix is None:
        return None

    matrixLength = len(matrix)
    jump: int = matrixLength - 1

    for _row in range(matrixLength - 1):
        for _column in range(jump):
            if _column < _row:
                origin = [_row, _row]
            else:
                origin = [_row, _column]
            current = []

            if jump == 1:
                rowFactor, columnFactor = 0, 1
            else:
                rowFactor = origin[1]
                columnFactor = jump - origin[1]

            temp: int = None
            counter = 0

            while current != origin:
                if current == []:
                    current = list.copy(origin)

                if temp is None:
                    numberToSwitch = matrix[current[0]][current[1]]
                else:
                    numberToSwitch = temp

                rowDestiny = current[1]
                if counter == 0 or counter == 3:
                    columnDestiny = current[1] + columnFactor
                else:
                    columnDestiny = current[1] - columnFactor

                counter = counter + 1

                temp = matrix[rowDestiny][columnDestiny]

                matrix[rowDestiny][columnDestiny] = numberToSwitch

                current[0], current[1] = rowDestiny, columnDestiny

                columnFactor, rowFactor = rowFactor, columnFactor

        jump = jump - 2
        if jump < 1:
            break
