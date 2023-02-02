

class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '<h1>404 Page Not Found</h1>'


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()
        request = {}

        for front in self.fronts:
            front(request)
        # print(request['data'])
        code, body = view(request)

        start_response(code, [('Content-type', 'text/html; charset=utf-8')])
        return [body.encode('utf-8')]
