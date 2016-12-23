from collections import namedtuple


operation = namedtuple(
    'operation', 'operator priority left_associativity is_binary')


class Operator(object):

    def __init__(self):
        super(Operator, self).__init__()
        self.__operators = {
            '~':  operation(operator=lambda x: ~int(x),   priority=9,
                            left_associativity=False, is_binary=False),
            '+':  operation(operator=lambda x: +x,        priority=9,
                            left_associativity=False, is_binary=False),
            '-':  operation(operator=lambda x: -x,        priority=9,
                            left_associativity=False, is_binary=False),
            '**': operation(operator=lambda x, y: x ** y, priority=8,
                            left_associativity=False, is_binary=True),
            '^':  operation(operator=lambda x, y: x ** y, priority=8,
                            left_associativity=False, is_binary=True),
            '*':  operation(operator=lambda x, y: x * y,  priority=7,
                            left_associativity=True, is_binary=True),
            '/':  operation(operator=lambda x, y: x / y,  priority=7,
                            left_associativity=True, is_binary=True),
            '%':  operation(operator=lambda x, y: x % y,  priority=7,
                            left_associativity=True, is_binary=True),
            '//': operation(operator=lambda x, y: x // y, priority=7,
                            left_associativity=True, is_binary=True),
            '+ ': operation(operator=lambda x, y: x + y,  priority=6,
                            left_associativity=True, is_binary=True),
            '- ': operation(operator=lambda x, y: x - y,  priority=6,
                            left_associativity=True, is_binary=True),
            '>>': operation(operator=lambda x, y: int(x) >> int(y), priority=5,
                            left_associativity=True, is_binary=True),
            '<<': operation(operator=lambda x, y: int(x) << int(y), priority=5,
                            left_associativity=True, is_binary=True),
            '&':  operation(operator=lambda x, y: int(x) & int(y),  priority=4,
                            left_associativity=True, is_binary=True),
            '|':  operation(operator=lambda x, y: int(x) | int(y),  priority=3,
                            left_associativity=True, is_binary=True),
            '#':  operation(operator=lambda x, y: int(x) ^ int(y),  priority=3,
                            left_associativity=True, is_binary=True),
            '>=': operation(operator=lambda x, y: x >= y, priority=2,
                            left_associativity=True, is_binary=True),
            '<=': operation(operator=lambda x, y: x <= y, priority=2,
                            left_associativity=True, is_binary=True),
            '>':  operation(operator=lambda x, y: x > y,  priority=2,
                            left_associativity=True, is_binary=True),
            '<':  operation(operator=lambda x, y: x < y,  priority=2,
                            left_associativity=True, is_binary=True),
            '<>': operation(operator=lambda x, y: x != y, priority=1,
                            left_associativity=True, is_binary=True),
            '==': operation(operator=lambda x, y: x == y, priority=1,
                            left_associativity=True, is_binary=True),
            '!=': operation(operator=lambda x, y: x != y, priority=1,
                            left_associativity=True, is_binary=True),
            ')':  operation(operator=None,                priority=0,
                            left_associativity=True, is_binary=False),
            '(':  operation(operator=None,                priority=0,
                            left_associativity=True, is_binary=True),
            ',':  operation(operator=lambda x, y: x + [y]
                            if isinstance(x, list) else [x, y],
                            priority=0, left_associativity=True,
                            is_binary=True)
            }

    def is_operator(self, token):
        return bool(self.__operators.get(token))

    def get_operation(self, token):
        return self.__operators.get(token)
