from views import Other, HomeView, Index, ContactView, PageNotFound404


routes = {
    '/': Index(),
    '/home/': HomeView(),
    '/other/': Other(),
    '/contact/': ContactView(),
    'error404': PageNotFound404(),
}
