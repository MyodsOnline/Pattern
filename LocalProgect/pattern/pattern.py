from copy import deepcopy


class CoursePrototype:

    def clone(self):
        return deepcopy(self)


class Course(CoursePrototype):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)


class InteractiveCourse(Course):

    def __init__(self, name, category):
        super().__init__(name, category)
        self.type = 'interactive'


class OnlineCourse(Course):

    def __init__(self, name, category):
        super().__init__(name, category)
        self.type = 'online'


class CourseFactory:
    course_types = {
        'interactive': InteractiveCourse,
        'online': OnlineCourse,
    }

    @classmethod
    def create_course(cls, type_, name, category):
        return cls.course_types[type_](name, category)


class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result

