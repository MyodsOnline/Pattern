from quopri import decodestring

from requests import GetRequest, PostRequest


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

        request = {}

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequest().get_request_params(environ)
            request['data'] = Application.decode_value(data)
            print(f'Нам пришёл post-запрос: {Application.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequest().get_request_params(environ)
            request['request_params'] = Application.decode_value(request_params)
            print(f'Нам пришли GET-параметры:'
                  f' {Application.decode_value(request_params)}')

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        for front in self.fronts:
            front(request)
        print(request)
        code, body = view(request)

        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for key, value in data.items():
            val = bytes(value.relpace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[key] = val_decode_str
        return new_data
