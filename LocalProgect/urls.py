from datetime import date
import json
import os

from views import Other, HomeView, Index


JSON_FILE_PATH = os.path.join('fixtures', 'data.json')


def load_json():
    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def secret_front(request):
    request['secret'] = date.today()


def other_front(request):
    request['key'] = 'Some awesome text'


def home_front(request):
    request['data'] = 'Some awesome text'


fronts = [secret_front, other_front, home_front]

routes = {
    '/': Index(),
    '/home/': HomeView(),
    '/other/': Other(),
}
