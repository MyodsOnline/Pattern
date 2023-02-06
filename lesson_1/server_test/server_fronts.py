from datetime import date


def title(request):
    request['title'] = 'Post page'


def secret_front(request):
    request['secret'] = date.today()


def other_front(request):
    request['key'] = 'Some awesome text'


def home_front(request):
    request['home'] = '<h1>Home view</h1>'


fronts = [secret_front, other_front, home_front, title]
