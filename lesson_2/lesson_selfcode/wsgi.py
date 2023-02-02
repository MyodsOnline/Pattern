from request import Request

class Framework:

    def __call__(self, environ, start_response):
        request = Request(environ)

        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from simple wsgi application']
