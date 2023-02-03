from wsgi import Framework
from url import Url
from view import View
from responce import Response


class MyFirstView(View):

    def get(self, request):
        return Response(body='GET SUCCESS')

    def post(self, request):
        return Response(status='201 Created', body='POST SUCCESS', headers={'Babayka': '123'})


urls = [
    Url('/homepage', MyFirstView)
]

app = Framework(urls)


#  gunicorn main:app -b :8001
