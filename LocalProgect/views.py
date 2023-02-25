from framework.templator import render
from logger.logger_config import Logger
from engine import Engine
from pattern.structural_patterns import AppRoutes, Debug
from pattern.behavioral_patterns import CreateView, ListView
from framework.server import FakeApplication


logger = Logger('views')
creation_logs = Logger('create')
site = Engine()

routes = {}


@AppRoutes(routes=routes, url='/')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        logger.log(f'Load Index page with {request["method"]}')
        return '200 OK', render(template_name='index.html',
                                title='Index page',
                                date=request.get('secret', None))


@AppRoutes(routes=routes, url='/other/')
class Other:
    @Debug(name='Other')
    def __call__(self, request):
        logger.log(f'Load Other page with {request["method"]}')
        return '200 OK', render(template_name='other.html',
                                title='Other page',
                                date=request.get('key'),
                                description=request.get('description'))


@AppRoutes(routes=routes, url='/home/')
class HomeView:
    @Debug(name='HomeView')
    def __call__(self, request):
        logger.log('Load Home page')
        return '200 OK', render(template_name='home.html',
                                title='Home page',
                                date=request.get('data'),
                                path=request.get('path'))


@AppRoutes(routes=routes, url='/contact/')
class ContactView:
    @Debug(name='ContactView')
    def __call__(self, request):
        logger.log('Load Post page')
        return '200 OK', render(template_name='contacts.html',
                                title='Post page')


@AppRoutes(routes=routes, url='error404')
class PageNotFound404:
    def __call__(self, request):
        logger.log('Load 404 page')
        return '404 WHAT', '<h1>404. Page Not Found</h1>'


@AppRoutes(routes=routes, url='/category-list/')
class CategoryList:
    @Debug(name='CategoryList')
    def __call__(self, request):
        logger.log('Список категорий')
        return '200 OK', render(template_name='category_list.html',
                                categories_list=site.categories_list,
                                title='Categories',)


@AppRoutes(routes=routes, url='/create-category/')
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
                                    title='Categories',)

        else:
            return '200 OK', render(template_name='create_category.html',
                                    categories_list=site.categories_list,
                                    title='Categories',)


@AppRoutes(routes=routes, url='/create-course/')
class CreateCourse:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'post':
            post_data = request['request_post_data']
            course_name = post_data['course_name']

            creation_logs.log(f'Create new category - {course_name}')

            course_name = site.decode_value(course_name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))
                print(category.courses)
                course = site.create_course('online', course_name, category)
                # add a variable course type
                site.courses.append(course)
                print(course.__dict__)

            return '200 OK', render(template_name='course_list.html',
                                    courses_list=category.courses,
                                    category_name=category.name,
                                    category_id=category.id,
                                    title='Courses')
        else:
            try:
                self.category_id = int(request['request_get_data']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render(template_name='create_course.html',
                                        category_name=category.name,
                                        category_id=category.id,
                                        title='Courses')
            except KeyError:
                return '200 OK', 'No categories have been added yet'


@AppRoutes(routes=routes, url='/courses-list/')
class CoursesList:
    @Debug(name='CoursesList')
    def __call__(self, request):
        try:
            category = site.find_category_by_id(
                int(request['request_get_data']['id']))
            return '200 OK', render(template_name='course_list.html',
                                    courses_list=category.courses,
                                    category_name=category.name,
                                    category_id=category.id,
                                    title='Courses')
        except KeyError:
            return '200 OK', 'No courses have been added yet'


@AppRoutes(routes=routes, url='/copy-course/')
class CopyCourse:
    def __call__(self, request):
        request_params = request['request_get_data']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_course = old_course.clone()
                new_course.name = f'copy_{name}'
                site.courses.append(new_course)

            return '200 OK', render(template_name='course_list.html',
                                    courses_list=site.courses,
                                    category_name=new_course.category.name,
                                    category_id=new_course.category.id,
                                    title='Courses')

        except KeyError:
            return '200 OK', 'No courses have been added yet'


@AppRoutes(routes=routes, url='/user-list/')
class StudentListView(ListView):
    queryset = site.students
    print(queryset)
    template_name = 'user_list.html'


@AppRoutes(routes=routes, url='/create-user/')
class UserCreateView(CreateView):
    template_name = 'create_user.html'

    def create_obj(self, data: dict):
        print(f'DATA FROM VIEW - {data}')
        name = site.decode_value(data['user_name'])
        role = site.decode_value(data['user_type_select'])
        new_obj = site.create_user(role, name)
        site.students.append(new_obj)
        print(f'Student {name} with {role} created')
