from datetime import datetime

from framework.query_requests import PostRequests, GetRequest


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        request = {'method': environ['REQUEST_METHOD'].lower()}

        if request['method'] == 'post':
            post_data = PostRequests().get_request_params(environ)
            # print(post_data)
            request['request_data'] = post_data
            self.write_file(post_data)
        if request['method'] == 'get':
            get_data = GetRequest().get_request_params(environ)
            # print(get_data)
            if len(get_data) > 0:
                request['request_data'] = get_data
                self.write_file(get_data)

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = self.routes['error404']

        for front in self.fronts:
            front(request)
        # print(request['data'])
        code, body = view(request)

        start_response(code, [('Content-type', 'text/html; charset=utf-8')])
        return [body.encode('utf-8')]

    def write_file(self, request_data):
        timestamp = datetime.now().strftime('%y.%m.%d %H:%M:%S')
        with open('fixtures/request.txt', 'a+', encoding='utf-8') as file:
            for k, v in request_data.items():
                line = f'{k}: {v}\n'
            file.write(f'{timestamp}: {line}')


# Новый вид WSGI-application.
# Первый — логирующий (такой же, как основной,
# только для каждого запроса выводит информацию
# (тип запроса и параметры) в консоль.
class DebugApplication(Application):

    def __init__(self, routes_obj, fronts_obj):
        self.application = Application(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        print('DEBUG MODE')
        print(env)
        return self.application(env, start_response)


# Новый вид WSGI-application.
# Второй — фейковый (на все запросы пользователя отвечает:
# 200 OK, Hello from Fake).
class FakeApplication(Application):

    def __init__(self, routes_obj, fronts_obj):
        self.application = Application(routes_obj, fronts_obj)
        super().__init__(routes_obj, fronts_obj)

    def __call__(self, env, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake']
