import re
from collections import namedtuple


argument = namedtuple('argument', 'value')


class Number(object):

    def __init__(self):
        super(Number, self).__init__()
        self.__numbers = {self.__is_decimal_number: lambda arg: float(arg),
                          self.__is_binary_number: lambda arg: int(arg, 2),
                          self.__is_octal_number: lambda arg: int(arg, 8),
                          self.__is_hex_number: lambda arg: int(arg, 16)
                          }

    def __is_decimal_number(self, token):
        try:
            float(token)
        except Exception as e:
            return False
        else:
            return True

    def __is_binary_number(self, token):
        if (re.search('^[+-]?0b[0-1]+$', token)):
            return True
        else:
            return False

    def __is_octal_number(self, token):
        if (re.search('^[+-]?0o[0-7]+$', token)):
            return True
        else:
            return False

    def __is_hex_number(self, token):
        if (re.search('^[+-]?0x[0-9a-f]+$', token)):
            return True
        else:
            return False

    def is_number(self, token):
        for number in sorted(self.__numbers):
            if number(token):
                return True

    def to_number(self, token):
        for number in sorted(self.__numbers.items()):
            if number[0](token):
                return number[1](token)
