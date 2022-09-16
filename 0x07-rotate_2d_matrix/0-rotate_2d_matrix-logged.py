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
    print(f'matrix len {matrixLength}')
    # avance inical
    jump: int = matrixLength - 1

    for _row in range(matrixLength - 1):
        print(f'row {_row}')
        print(f'jump is {jump}')
        _column = _row

        while _column < (jump + _row):
            
        #for _column in range(jump):
            print(f'the column is {_column}')
            print(f'el salto es {jump}')
            # set origin
            # if _column < _row:
            #     origin = [_row, _row]
            # else:
            #     origin = [_row, _column]

            origin = [_row, _column]

            print(f'the origin is {origin}')
            current = []

            # if jump == 1:
            #     rowFactor, columnFactor = 0, jump
            # elif jump == 2:
            #     if origin[1] - origin[0] == 1:
            #         rowFactor, columnFactor = 1, 1
            #     elif origin[1] - origin[0] == 0:
            #         rowFactor, columnFactor = 0, 2
            #     else:
            #         rowFactor, columnFactor = 2, 0
            # else:
            #     rowFactor = origin[1]
            #     columnFactor = jump - origin[1]

            rowFactor = origin[1] - origin[0]
            columnFactor = jump - rowFactor
            
                # parametros por defecto
            temp: int = None
            counter = 0

            while current != origin:
                print('inicia el proceso')
                print(f'counter {counter}')
                # set initial position
                if current == []:
                    current = list.copy(origin)

                print(current)
                print(f'reading position  {current[0]}, {current[1]}')

                # set the number to switch
                if temp is None:
                    numberToSwitch = matrix[current[0]][current[1]]
                else:
                    numberToSwitch = temp
                print(f'the number to switch is {numberToSwitch}')

                # set the destiny
                rowDestiny = current[1]
                if counter == 0 or counter == 3:
                    columnDestiny = current[1] + columnFactor
                else:
                    columnDestiny = current[1] - columnFactor

                counter = counter + 1

                print(f'columnfactor {columnFactor}, rowFactor {rowFactor}')
                print(f'destiny {rowDestiny}, {columnDestiny}')

                # storing the number  of the destiny in a tmp
                temp = matrix[rowDestiny][columnDestiny]
                print(f'the stored number of the target position  {temp}')

                # swithcing number
                matrix[rowDestiny][columnDestiny] = numberToSwitch
                print('position changed')

                # set new origin for the next iteration
                current[0], current[1] = rowDestiny, columnDestiny
                # set new factors
                columnFactor, rowFactor = rowFactor, columnFactor

                print(f'the new current {current}')
                print(f'the new matrix es {matrix}')
                print()
                print()
                print()
                print()
            _column = _column + 1

            for line in matrix:
                print(line)
        jump = jump - 2
        if jump < 1:
            break
