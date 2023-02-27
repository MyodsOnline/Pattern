from quopri import decodestring

from pattern.creational_patterns import CourseFactory, Category, UserFactory


class Engine:

    def __init__(self):
        self.categories_list = []
        self.courses = []
        self.teachers = []
        self.students = []

    @staticmethod
    def create_user(type_, name):
        return UserFactory.create(type_, name)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    @staticmethod
    def create_course(type_, name, category):
        return CourseFactory.create_course(type_, name, category)

    def find_category_by_id(self, id):
        for item in self.categories_list:
            if item.id == id:
                return item
        raise Exception(f'Not found category with id = {id}')

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return Exception(f'Course {name} not found.')

    def get_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return Exception(f'User {name} not found.')

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = decodestring(val_b)
        return val_decode_str.decode('UTF-8')
