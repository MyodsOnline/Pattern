from framework.templator import render
from logger.logger_config import Logger
from engine import Engine


logger = Logger('views')
site = Engine()


class Index:
    def __call__(self, request):
        logger.log(f'Load Index page with {request["method"]}')
        return '200 OK', render(template_name='index.html',
                                title = 'Index page',
                                date=request.get('secret', None))


class Other:
    def __call__(self, request):
        logger.log(f'Load Other page with {request["method"]}')
        return '200 OK', render(template_name='other.html',
                                title = 'Other page',
                                date=request.get('key'),
                                description = request.get('description'))


class HomeView:
    def __call__(self, request):
        logger.log('Load Home page')
        return '200 OK', render(template_name='home.html',
                                title = 'Home page',
                                date = request.get('data'),
                                path = request.get('path'))


class ContactView:
    def __call__(self, request):
        logger.log('Load Post page')
        return '200 OK', render(template_name='contacts.html',
                                title='Post page')


class PageNotFound404:
    def __call__(self, request):
        logger.log('Load 404 page')
        return '404 WHAT', '<h1>404. Page Not Found</h1>'
