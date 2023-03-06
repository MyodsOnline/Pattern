# behavioral patterns
# 1. chain_of_responsibility

from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class Decoder(Handler):

    def __init__(self):
        self._next = None
        self.encoding = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, request):
        try:
            print(f'Try to decode string {self.encoding}')
            return request.decode(self.encoding)
        except:
            print(f'cant decode in {self.encoding}')
            if self._next:
                return self._next.handler(request)


class Cp1251(Decoder):
    def __init__(self):
        super().__init__()
        self.encoding = 'cp1251'


class UTF8(Decoder):
    def __init__(self):
        super().__init__()
        self.encoding = 'utf8'


class Final(Decoder):
    def __init__(self):
        super().__init__()
        self.encoding = 'utf8'

    def handle(self, request):
        return f'cant decode {request}'


data = b'\x78'

cp1251 = Cp1251()
utf8 = UTF8()
final = Final()

utf8.set_next(cp1251).set_next(final)
print(utf8.handle(data))
