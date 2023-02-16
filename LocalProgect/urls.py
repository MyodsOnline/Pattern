from views import Other, HomeView, Index, ContactView, PageNotFound404


routes = {
    '/': Index(),
    '/home/': HomeView(),
    '/other/': Other(),
    '/contact/': ContactView(),
    'error404': PageNotFound404(),

    '/study_programs/': 'StudyPrograms()',
    '/courses-list/': 'CoursesList()',
    '/create-course/': 'CreateCourse()',
    '/create-category/': 'CreateCategory()',
    '/category-list/': 'CategoryList()',
    '/copy-course/': 'CopyCourse()',
}
