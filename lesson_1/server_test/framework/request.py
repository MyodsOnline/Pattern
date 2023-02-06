import urllib.parse


class Request:

    def __init__(self, environ: dict):
        self.method = environ['REQUEST_METHOD'].lower()
        self.path = environ['PATH_INFO']
        self.headers = self._get_headers(environ)
        self.query_params = self._get_query_params(environ)

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP'):
                headers[key[5:]] = value
        return headers

    def _get_query_params(self, environ):
        query_params = {}
        query_string = environ.get('QUERY_STRING')

        if not query_string:
            return {}

        query_string = query_string.split('&')
        print(query_string)

        for q_str in query_string:
            print('---->', q_str)
            key, value = q_str.split('=')
            if query_params.get(key):
                query_params[key].append(value)
            else:
                query_params[key] = [value]

        return query_params


class PostRequests:

    @staticmethod
    def parse_input_data(data: str):
        data = urllib.parse.unquote_plus(data)

        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        print('content_length:', content_length)

        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            print(f'{data_str}')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
