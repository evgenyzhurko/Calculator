import importlib
from numbers import Number


class Constant(object):

    def __init__(self, modules=()):
        super(Constant, self).__init__()
        self.__constants = {}
        self.__modules = modules
        self.__import_constant()

    def __import_constant(self):
        number = Number()
        for module_name in self.__modules:
            module = importlib.import_module(module_name)
            for constant in filter(lambda x: number.is_number(
                                   str(getattr(module, x))), dir(module)):
                self.__constants[constant.lower()] = getattr(module, constant)

    def is_constant(self, token):
        return bool(self.__constants.get(token))

    def get_constant(self, token):
        return self.__constants.get(token)
