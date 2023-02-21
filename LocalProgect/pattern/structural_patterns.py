from datetime import datetime
from time import time


class AppRoutes:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()


class Debug:

    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def timeit(method):
            def timed(*args, **kwargs):
                time_start = datetime.now().strftime('%y.%m.%d %H:%M:%S')
                ts = time()
                result = method(*args, **kwargs)
                te = time()
                delta = te - ts
                print(f'{time_start} |----> The request to "{self.name}" took {delta:2.2f} ms to complete.')
                return result
            return timed
        return timeit(cls)