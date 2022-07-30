#!/usr/bin/python3
"""
returns the pascal triangle in a list of lists
"""


def pascal_triangle(n):
    """
    main function

    n:
    number of rows to build the pascal triangle

    returns:
    a list of lists
    """

    triangle = []
    rows = n
    row = 0

    while (row < rows):
        rowNumbers = []
        pos = 0
        number = 1

        if (row == 0):
            rowNumbers.insert(pos, number)

        while (pos <= row-1):
            if (pos == 0):
                rowNumbers.insert(pos, number)
                rowNumbers.insert(row-1, number)
            else:
                number = triangle[row-1][pos-1] + triangle[row-1][pos]
                rowNumbers.insert(pos, number)

            pos += 1

        triangle.append(rowNumbers)
        row += 1

    return triangle
