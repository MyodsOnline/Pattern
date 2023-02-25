from copy import deepcopy


class User:
    def __init__(self, name):
        self.name = name


class Teacher(User):
    pass


class Student(User):
    def __init__(self, name):
        self.courses = []
        super().__init__(name)


class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher,
    }

    @classmethod
    def create(cls, type_, name):
        print(f'FROM PATTERN {type_}, {name}')
        return cls.types[type_](name)


class CoursePrototype:

    def clone(self):
        return deepcopy(self)


class Course(CoursePrototype):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)
        student.courses.append(self)


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
        Category.incr_id()
        self.id = Category.auto_id
        self.name = name
        self.category = category
        self.courses = []

    @staticmethod
    def incr_id():
        Category.auto_id += 1

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result
