import importlib
from collections import namedtuple


function = namedtuple('function', 'function priority left_associativity')


class Function(object):

    def __init__(self, modules=()):
        super(Function, self).__init__()
        self.__functions = {
            'abs': function(
                function=abs, priority=10, left_associativity=True),
            'round': function(
                function=round, priority=10, left_associativity=True),
            'pow': function(
                function=pow, priority=10, left_associativity=True),
            }
        self.__modules = modules
        self.__import_function()

    def __import_function(self):
        for module_name in self.__modules:
            module = importlib.import_module(module_name)
            for func in filter(lambda x: hasattr(getattr(module, x),
                               '__call__'), dir(module)):
                self.__functions[func.lower()] = function(
                    function=getattr(module, func),
                    priority=10,
                    left_associativity=True)

    def is_function(self, token):
        return bool(self.__functions.get(token))

    def get_function(self, token):
        return self.__functions.get(token)
