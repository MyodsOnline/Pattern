from datetime import date
import json
import os


JSON_FILE_PATH = os.path.join('fixtures', 'data.json')


def load_json():
    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def secret_front(request):
    request['secret'] = date.today()


def other_front(request):
    request['key'] = [(f"{key}: {value}\n").encode("utf-8")
                      for key, value in os.environ.items()]


def home_front(request):
    request['data'] = load_json()


fronts = [secret_front, other_front, home_front]