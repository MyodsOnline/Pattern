from datetime import datetime
import os


class SingletonByName(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instances = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name not in cls.__instances:
            cls.__instances[name] = super().__call__(*args, **kwargs)
        return cls.__instances[name]


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        file = f'{self.name}.log'
        path = os.path.join('logger', file)
        with open(path, 'a') as f:
            f.write(f'{datetime.now()}  {text}\n')
