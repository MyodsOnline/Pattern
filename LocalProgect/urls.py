from datetime import date
from views import Other, HomeView, Index


def secret_front(request):
    request['secret'] = date.today()


def other_front(request):
    request['key'] = 'Some awesome text'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/home/': HomeView(),
    '/other/': Other(),
}
