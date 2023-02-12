from datetime import date
import json
import os
from logger.logger_config import Logger


JSON_FILE_PATH = os.path.join('fixtures', 'data.json')
logger = Logger('server')


def logger_front(request, environ=None):
    if environ:
        logger.log(f'{environ["REMOTE_ADDR"]} {environ["REQUEST_METHOD"]} {environ["PATH_INFO"]}')
    return


def load_json():
    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def secret_front(request):
    request['secret'] = date.today().strftime('%d.%m.%Y')


def other_front(request):
    request['key'] = [(f"{key}: {value}\n").encode("utf-8")
                      for key, value in os.environ.items()]
    request['description'] = f"Вывод переменной environ['PATH_INFO'] из базовой логики приложения:"


def home_front(request):
    request['data'] = load_json()
    request['path'] = f'{os.path.basename(JSON_FILE_PATH)}'


fronts = [secret_front, other_front, home_front, logger_front]
