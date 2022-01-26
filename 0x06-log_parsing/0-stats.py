#!/usr/bin/python3
# """ reads stdin line by line and computes metrics"""

# import sys
# import datetime

# status_table = ['200', '301', '400', '401', '403', '404', '405', '500']
# reg_table = {'200': 0,
#              '301': 0,
#              '400': 0,
#              '401': 0,
#              '403': 0,
#              '404': 0,
#              '405': 0,
#              '500': 0
#              }


# def format_validator(list):
#     """validate the format of input string"""

#     phrase = (list[4] + " " + list[5] + " " + list[6])[1:-1]
#     date = (list[2] + " " + list[3])[1:-1]

#     if (type(list[0]) != str or list[1] != '-'):
#         return False

#     # if list[1] != '-':
#     #    return False

#     if (phrase != "GET /projects/260 HTTP/1.1"):
#         return False

#     if list[7] not in status_table:
#         return False

#     if type(int(list[8])) != int:
#         return False

#     try:
#         datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
#     except ValueError:
#         return False

#     return True


# def print_statics(reg_table, size):
#     """print the statics in stdout"""

#     print("File size: {}".format(size))
#     for k, v in reg_table.items():
#         if v != 0:
#             v = str(v)
#             print("{}: {}".format(k, v))


# def log():
#     """pricipal function"""
#     size = 0
#     counter = 0
#     try:
#         for line in sys.stdin:
#             line_args = line.split()

#             if format_validator(line_args) is True:
#                 reg_table[line_args[7]] += 1
#                 size += int(line_args[8])
#                 counter += 1

#                 if counter == 10:
#                     print_statics(reg_table, size)
#                     counter = 0
#             else:
#                 pass

#     except KeyboardInterrupt:
#         print_statics(reg_table, size)


# # entry point
# log()


import sys


class Log:
    """ holds important attributes for loging """

    def __init__(self):
        """ init """
        empty_cache = {}
        li = [200, 301, 400, 401, 403, 404, 405, 500]
        for l in li:
            empty_cache[str(l)] = 0
        self.empty_cache = empty_cache.copy()
        self.id = 1
        self.cache = empty_cache.copy()
        self.size = 0
        self.i = 0

    def do_stuff(self):
        """ do stuff """
        i = 0
        for line in sys.stdin:
            ls = line.split(' ')
            '''print(ls)
            print(len(ls))'''
            '''print(ls)'''
            if len(ls) < 2:
                '''self.size += eval(ls[8].strip('\n'))
                self.i += 1'''
                continue
            code = ls[-2]
            '''print("code: [{}]".format(code))
            print("cachecode1: [{}]".format(self.cache[code]))'''
            '''if self.cache.get(code) is None:
                self.cache.update({code: 1})
            else:'''
            if code in self.cache.keys():
                self.cache[code] += 1
            '''self.cache[code] += 1'''
            '''self.cache['cool'] += 2'''
            '''print("cachecode2: [{}]".format(self.cache[code]))
            print("--------")'''
            self.size += int(ls[-1].strip('\n'))
            self.i += 1
            if self.i == 10:
                self.i = 0
                self.print_dat()
                '''self.cache = self.empty_cache.copy()'''
        sys.stdout.flush()

    def print_dat(self):
        """ Prints dat cache """
        print("File size: {:d}".format(self.size))
        for k in sorted(self.cache.keys()):
            if self.cache[k] != 0:
                print("{}: {}".format(k, self.cache[k]))
        '''self.cache = self.empty_cache.copy()'''


log = Log()
try:
    log.do_stuff()
    log.print_dat()
except KeyboardInterrupt:
    log.print_dat()
    raise
