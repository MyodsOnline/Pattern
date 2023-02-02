from framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render(template_name='index.html', date=request.get('secret', None))


class Other:
    def __call__(self, request):
        print(request)
        return '200 OK', render(template_name='other.html', date=request.get('key'))


class HomeView:
    def __call__(self, request):
        print(f"Request data when HomeView - {request['data']}")
        return '200 OK', render(template_name='home.html', date=request.get('data'))
