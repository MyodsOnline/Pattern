from wsgi import Framework
from url import Url
from view import View


class MyFirstView(View):

    def get(self, request):
        return 'Im get request'

    def post(self, request):
        return 'Im post request'


urls = [
    Url('homepage/', MyFirstView)
]

app = Framework(urls)


#  gunicorn main:app -b :8001
