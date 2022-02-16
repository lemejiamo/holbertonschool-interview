#!/usr/bin/python3
""" method that determines if a given
    data set represents a valid UTF-8 encoding. """


def validUTF8(data):
    """
    - Return: True if data is a valid UTF-8 encoding.
    - else return False.
    - character in UTF-8 can be 1 to 4 bytes long.
    - Each integer represents 1 byte of data,
    therefore you only need to handle
    the 8 least significant bits of each integer """
    num_bytes = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]
        if num_bytes == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                num_bytes += 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        num_bytes -= 1

    return num_bytes == 0
