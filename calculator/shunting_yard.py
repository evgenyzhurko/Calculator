from numbers import Number, argument
from operators import Operator, operation
from functions import Function, function
from constants import Constant


class ShuntingYard(object):

    def __init__(self, modules):
        super(ShuntingYard, self).__init__()
        self.__numbers = Number()
        self.__operators = Operator()
        self.__functions = Function(modules)
        self.__constants = Constant(modules)

    def algorithm(self, expression):
        revers_polish_notation = []
        operator_stack = []
        for token in expression:
            if self.__numbers.is_number(token):
                revers_polish_notation.append(
                    argument(value=self.__numbers.to_number(token)))
            elif self.__functions.is_function(token):
                operator_stack.append(self.__functions.get_function(token))
            elif self.__constants.is_constant(token):
                revers_polish_notation.append(
                    argument(value=self.__constants.get_constant(token)))
            elif token is '(':
                operator_stack.append(self.__operators.get_operation('('))
            elif token is ')':
                while operator_stack[-1] != self.__operators.get_operation('('):
                    revers_polish_notation.append(operator_stack.pop())
                operator_stack.pop()
            elif self.__operators.is_operator(token):
                current_operation = self.__operators.get_operation(token)
                while (len(operator_stack) > 0
                       and operator_stack[-1].priority > 0
                       and ((current_operation.left_associativity is True
                            and current_operation.priority <=
                            operator_stack[-1].priority)
                       or (current_operation.left_associativity is False
                           and current_operation.priority <
                           operator_stack[-1].priority))):
                    revers_polish_notation.append(operator_stack.pop())
                operator_stack.append(self.__operators.get_operation(token))
        while len(operator_stack) > 0:
            revers_polish_notation.append(operator_stack.pop())
        return revers_polish_notation
