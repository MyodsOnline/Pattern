from framework.templator import render
#update
from framework.request import Request


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('secret', None))


class HomeView:
    def __call__(self, request):
        return '200 OK', render('home.html', date=request.get('home', None))


class Other:
    def __call__(self, request):
        return '200 OK', render('other.html', date=request.get('key', None))


class Post:
    def __call__(self, request):
        return '200 OK', render('post.html', site_title=request.get('title', None), date=request.get('key', None))


# update later
class View:

    def get(self, request, *args, **kwargs):
        print('Im get request')

    def post(self, request, *args, **kwargs):
        print('Im post request')