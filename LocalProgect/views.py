from framework.templator import render
from logger.logger_config import Logger
from engine import Engine


logger = Logger('views')
creation_logs = Logger('create')
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


class CategoryList:
    def __call__(self, request):
        logger.log('Список категорий')
        return '200 OK', render(template_name='category_list.html',
                                categories_list=site.categories_list,
                                title = 'Categories',)


class CreateCategory:
    def __call__(self, request):
        if request['method'] == 'post':
            data = request['request_post_data']
            if len(data['category_name']) > 0:
                category_name = data['category_name']
            else:
                category_name = 'Empty name'

            creation_logs.log(f'Create new category - {category_name}')

            category_name = site.decode_value(category_name)

            category_id = data.get('category_id')
            category = None

            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(category_name, category)
            site.categories_list.append(new_category)

            return '200 OK', render(template_name='category_list.html',
                                    categories_list=site.categories_list,
                                    title = 'Categories',)

        else:
            return '200 OK', render(template_name='create_category.html',
                                    categories_list=site.categories_list,
                                    title = 'Categories',)
