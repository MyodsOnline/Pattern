import urllib.parse


class GetRequest:

    @staticmethod
    def parse_data(data: str):
        data = urllib.parse.unquote_plus(data)
        result = {}

        if data:
            params = data.split('&')
            for param in params:
                k, v = param.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        query_string = environ['QUERY_STRING']
        request_params = GetRequest.parse_data(query_string)
        return request_params


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
        # print('content_length:', content_length)

        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            # print(f'{data_str}')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
