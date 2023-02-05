from wsgiref.simple_server import make_server

from framework.server import Application
from server_urls import routes, fronts

# update
from server_urls_upd import Url
from server_views import View


application = Application(routes, fronts)

with make_server('', 8000, application) as localhost:
    print("Application start at http://127.0.0.1:8000")
    localhost.serve_forever()
