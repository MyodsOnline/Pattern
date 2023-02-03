class Response:
    def __init__(self, body=None, status='200 OK', headers=None):
        self.status = status
        self.headers = self._set_headers(headers)
        self.body = body

    def _set_headers(self, user_headers):
        headers = {
            'Content-Type': 'text/html'
        }

        if user_headers:
            headers.update(user_headers)

        return headers
