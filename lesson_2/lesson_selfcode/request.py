class Request:

    def __init__(self, environ: dict):
        self.method = environ['REQUEST_METHOD'].lower()
        self.path = environ['PATH_INFO']
        self.headers = self._get_headers(environ)
        self.query_params = self._get_query_params(environ)
        print(environ)


    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP'):
                headers[key[5:]] = value

        return headers


    def _get_query_params(self, environ):
        query_params = {}
        qs = environ.get('QUERY_STRING')

        if not qs:
            return {}

        qs = qs.split('&')
        # print(qs)

        for q_str in qs:
            print('---->', q_str)
            key, value = q_str.split('=')
            if query_params.get(key):
                query_params[key].append(value)
            else:
                query_params[key] = [value]

        return query_params

