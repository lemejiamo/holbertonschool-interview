#!/usr/bin/python3
""" reads stdin line by line and computes metrics"""


import fileinput
import datetime

status_table = ['200', '400', '401', '403', '404', '405', '500', '301']
reg_table = {'200': 0,
             '400': 0,
             '401': 0,
             '403': 0,
             '404': 0,
             '405': 0,
             '500': 0,
             '301': 0
             }


def format_validator(list):
    """validate the format of input string"""

    if type(list[0]) != str:
        return False

    if list[1] != '-':
        return False

    date = (list[2] + " " + list[3])[1:-1]

    try:
        datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        return False

    phrase = (list[4] + " " + list[5] + " " + list[6])[1:-1]

    if (phrase != "GET /projects/260 HTTP/1.1"):
        return False

    if list[7] not in status_table:
        return False

    if type(int(list[8])) != int:
        return False

    return True


def print_statics(reg_table, size):
    """print the statics in stdout"""

    print("File size: {}".format(size))
    for k, v in reg_table.items():
        v = str(v)
        print("{}: {}".format(k, v))


try:
    data = fileinput.input()
    size = 0
    counter = 0

    for line in data:
        line_args = line.split()

        if format_validator(line_args) is True:
            reg_table[line_args[7]] += 1
            size += int(line_args[8])
            counter += 1

            if counter == 10:
                print_statics(reg_table, size)
                counter = 0
        else:
            pass


except KeyboardInterrupt:
    print_statics(reg_table, size)
