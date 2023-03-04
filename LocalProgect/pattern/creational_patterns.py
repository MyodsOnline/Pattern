from copy import deepcopy

from Pattern.LocalProgect.pattern.behavioral_patterns import Subject
from Pattern.LocalProgect.pattern.unit_of_work import DomainObject


class User:
    def __init__(self, name):
        self.name = name


class Teacher(User):
    def __init__(self, name):
        self.courses = []
        super().__init__(name)


class Student(User, DomainObject):
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
        return cls.types[type_](name)


class CoursePrototype:

    def clone(self):
        return deepcopy(self)


class Course(CoursePrototype, Subject):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)
        self.students = []
        super().__init__()

    def __getitem__(self, item):
        return self.students[item]

    def add_student(self, student: Student):
        self.students.append(student)
        student.courses.append(self)
        self.notify()


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
