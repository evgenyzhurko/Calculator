#!/usr/bin/env python2

import expression
from sys import argv


def evaluate(arg, *modules):
    try:
        e = expression.Expression(('math',) + modules)
        return e.calculate(arg)
    except Exception as e:
        print 'Error:', e.message


def calculate_shell():
    try:
        if len(argv) < 2:
            raise TypeError('calc takes exactly 1 arguments ({0} given)'.
                            format(len(argv) - 1))
        else:
            modules = []
            i = 0
            while i < (len(argv) - 2):
                modules.append(argv[i + 2])
                i += 1
            print evaluate(argv[1], *modules)
    except Exception as e:
        print 'Error:', e.message


if __name__ == '__main__':
    calculate_shell()
