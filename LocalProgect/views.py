from framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('secret', None))


class Other:
    def __call__(self, request):
        return '200 OK', render('other.html', date=request.get('key'))


class HomeView:
    def __call__(self, request):
        print(request['data'])
        return '200 OK', render('home.html', date=request.get('data'))
