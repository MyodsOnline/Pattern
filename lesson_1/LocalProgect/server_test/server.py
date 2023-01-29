from wsgiref.simple_server import make_server


def index_view():
    return '200 OK', [b'<h1>This page?</h1>']


def abc_view():
    return '200 OK', [b'ABC']


def home_view():
    return '200 OK', [b'Home view added']


def not_found_404_view():
    return '404 WHAT', [b'404 Page Not Found']


class Other:
    def __call__(self):
        return '200 OK', [b'<h1>other</h1><h3>text</h3>']


routes = {
    '/': index_view,
    '/abc/': abc_view,
    '/home/': home_view,
    '/other/': Other(),
}

class Application:
    def __init__(self, routes):
        print(routes)  # {'/': <function index_view>, '/abc/': <function abc_view>, '/home/': <function home_view>}
        self.routes = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_404_view
        code, body = view()  # <class 'str'> 200 OK, <class 'list'> [b'This page?']
        start_response(code, [('Content-Type', 'text/html')])
        return body


app = Application(routes)






with make_server('', 8000, app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
