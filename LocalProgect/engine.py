from pattern.pattern import CourseFactory


class Category:

    def __init__(self, name, category):
        self.name = name
        self.category = category


class Engine:

    def __init__(self):
        self.categories = []
        self.courses = []

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    @staticmethod
    def create_course(type_, name, category):
        return CourseFactory.create_course(type_, name, category)

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return Exception(f'Course {name} not found.')
