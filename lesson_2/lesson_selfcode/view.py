from responce import Response


class View:

    def get(self, request, *args, **kwargs) -> Response:
        print('Im get request')

    def post(self, request, *args, **kwargs) -> Response:
        print('Im post request')
