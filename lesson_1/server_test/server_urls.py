from datetime import date
from server_views import Other, HomeView, Index


def secret_front(request):
    request['secret'] = date.today()


def other_front(request):
    request['key'] = 'Some awesome text'


def home_front(request):
    request['home'] = '<h1>Home view</h1>'


fronts = [secret_front, other_front, home_front]

routes = {
    '/': Index(),
    '/home/': HomeView(),
    '/other/': Other(),
}
