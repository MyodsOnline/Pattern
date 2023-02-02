from wsgiref.simple_server import make_server


def application(environ, start_response):
    """
    :param environ: class 'dict', contains all environ params. first we need 'PATH_INFO'
    :param start_response: class 'method' of wsgiref.simple_server
    :return: bytes to show on page
    """

    path = environ['PATH_INFO']

    if path == '/':
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        return [b'Hello world from a simple WSGI application!']

    elif path == '/abc/':
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        ret = [(f"{key}: {value}\n").encode("utf-8")
               for key, value in environ.items()]
        return ret

    else:
        start_response('404 NOT FOUND', [('text/plain; charset=utf-8')])
        return [b'404 Not Found']


with make_server('', 8000, application) as httpd:
    # runs server on localhost on port 8000
    print("Serving on port 8000...")
    httpd.serve_forever()
