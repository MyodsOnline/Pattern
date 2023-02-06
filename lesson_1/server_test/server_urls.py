from server_views import Other, HomeView, Index, Post


routes = {
    '/': Index(),
    '/home/': HomeView(),
    '/other/': Other(),
    '/post/': Post(),
}
