from Pattern.lesson_1.server_test.framework.request import Request, PostRequests


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '<h1>404 Page Not Found</h1>'


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        request = Request(environ)
        print(f'1 - {request.headers}\n //// METHOD - {request.method}')

        if request.method == 'post':
            data = PostRequests().get_request_params(environ)
            print(f'POST data - {data}')
            with open('stdout/post_request.txt', 'w', encoding='utf-8') as post_r:
                for k, v in data.items():
                    line = f'{k}: {v}\n'
                    post_r.write(line)
        if request.method == 'get':
            data = Request(environ)._get_query_params(environ)
            print(f'GET data - {data}')
            with open('stdout/get_request.txt', 'w', encoding='utf-8') as get_r:
                for k, v in data.items():
                    line = f'{k}: {v}\n'
                    get_r.write(line)

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()
        request = {}

        for front in self.fronts:
            front(request)
        # print(f'Request - {request}')
        code, body = view(request)

        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
