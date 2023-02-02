class Request:

    def __init__(self, environ: dict):
        self.method = environ['REQUEST_METHOD'].lower()
        self.path = environ['PATH_INFO']
        self.headers = self._get_headers(environ)
        self._query_params = self._get_query_params(environ)
        print(environ)


    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP'):
                print(key)
                headers[key[5:]] = value

        return headers


    def _get_query_params(self, environ):
        query_params = {}
        qs = environ.get('QUERY_STRING')
        print(qs)

        return {}
