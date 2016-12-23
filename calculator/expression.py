from numbers import Number, argument
from operators import Operator, operation
from functions import Function, function
from constants import Constant
from shunting_yard import ShuntingYard
import inspect
import sys


class Expression(object):

    def __init__(self, modules):
        super(Expression, self).__init__()
        self.__modules = tuple(modules)
        self.__numbers = Number()
        self.__operators = Operator()
        self.__functions = Function(self.__modules)
        self.__constants = Constant(self.__modules)

    def __to_lowercase(self, expression_string):
        return expression_string.lower()

    def __remove_spaces(self, expression_string):
        return expression_string.replace(" ", "")

    def __check_brackets(self, expression_list):
        open_brackets = len(filter(lambda x: '(' is x, expression_list))
        close_brackets = len(filter(lambda x: ')' is x, expression_list))
        if (open_brackets != close_brackets):
            raise ValueError('brackets are not balanced')

    def __replace_operators(self, expression_string):
        expression_string = expression_string.replace('+', '+ ')
        expression_string = expression_string.replace('-', '- ')
        return expression_string

    def __insert_multiplication_operator(self, expression_list):
        i = 1
        while i < len(expression_list):
            if ((expression_list[i] is '(' and
                    (self.__numbers.is_number(expression_list[i - 1])
                        or expression_list[i - 1] is ')'))
                    or (expression_list[i - 1] is ')'
                        and self.__numbers.is_number(expression_list[i]))):
                expression_list.insert(i, '*')
            i += 1
        return expression_list

    def __find_unary_operator(self, expression_list):
        if expression_list[0] == '+ ' or expression_list[0] == '- ':
            expression_list[0] = expression_list[0][:1]
        for i in range(1, len(expression_list)):
            if ((expression_list[i] == '+ ' or expression_list[i] == '- ')
                    and self.__operators.is_operator(expression_list[i - 1])
                    and self.__operators.get_operation(
                        expression_list[i - 1]).is_binary):
                expression_list[i] = expression_list[i][:1]
        return expression_list

    def __pre_convert_operation(self, expression_string):
        for operation in [self.__to_lowercase,
                          self.__remove_spaces,
                          self.__replace_operators]:
            expression_string = operation(expression_string)
            if not expression_string:
                raise ValueError('expression is empty')
        return expression_string

    def __post_convert_operation(self, expression_list):
        for operation in [self.__insert_multiplication_operator,
                          self.__find_unary_operator,
                          self.__check_brackets]:
            expression_list = operation(expression_list)
        return expression_list

    def __is_token(self, token):
        return self.__numbers.is_number(token)\
            or self.__operators.is_operator(token)\
            or self.__functions.is_function(token)\
            or self.__constants.is_constant(token)

    def __convert(self, expression_string):
        expression_string = self.__pre_convert_operation(expression_string)
        expression_list = []
        start_position = 0
        while start_position < len(expression_string):
            for end_position in reversed(range(start_position,
                                               len(expression_string) + 1)):
                token = expression_string[start_position:end_position]
                if self.__is_token(token):
                    expression_list.append(token)
                    start_position += len(token)
                    break
            else:
                raise ValueError(
                    'expression contains unknown operator: \'{0}\''.
                    format(expression_string[start_position:
                                             len(expression_string)]))
        explression_list = self.__post_convert_operation(expression_list)
        return expression_list

    def __call_function(self, name, arguments):
        argument = arguments.pop()
        if not isinstance(argument, list):
            argument = [argument]
        arguments.append(name(*argument))

    def __call_operator(self, name, arguments):
        argument = []
        for i in range(len(inspect.getargspec(name).args)):
            argument.insert(0, arguments.pop())
        arguments.append(name(*argument))

    def calculate(self, expression):
        expression = self.__convert(expression)
        expression = ShuntingYard(self.__modules).algorithm(expression)
        arguments = []
        try:
            for token in expression:
                if isinstance(token, argument):
                    arguments.append(token.value)
                elif isinstance(token, operation):
                    self.__call_operator(token.operator, arguments)
                elif isinstance(token, function):
                    self.__call_function(token.function, arguments)
        except IndexError as e:
            raise IndexError('incorrect expression')
        return arguments[0]
