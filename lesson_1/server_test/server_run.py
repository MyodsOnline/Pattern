from wsgiref.simple_server import make_server

from framework.server import Application
from server_urls import routes, fronts


application = Application(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Application start")
    httpd.serve_forever()
