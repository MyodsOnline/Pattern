from wsgiref.simple_server import make_server

# from framework.main import Framework
# from urls import routes, fronts
#
#
# application = Framework(routes, fronts)


def index_view():
    return '200 OK', [b'This page?']


def abc_view():
    return '200 OK', [b'ABC']


def home_view():
    return '200 OK', [b'Home view added']


def not_found_404_view():
    return '404 WHAT', [b'404 PAGE Not Found']


routes = {
    '/': index_view,
    '/abc/': abc_view,
    '/home/': home_view,
}


class Application:

    def __init__(self, routes):
        print(routes)
        self.routes = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_404_view
        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return body




app = Application(routes)

# def app(environ, start_response):
#     path = environ['PATH_INFO']
#     if path == '/':
#         start_response('200 OK', [('Content-Type', 'text/html')])
#         return [b'Index it returns']
#     elif path == '/abc/':
#         start_response('200 OK', [('Content-Type', 'text/html')])
#         return [b'ABC']
#     else:
#         start_response('404 Not Found', [('Content-Type', 'text/html')])
#         return [b'404 Not Found']






with make_server('', 8000, app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
