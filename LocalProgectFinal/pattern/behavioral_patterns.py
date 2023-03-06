from framework.templator import render


class TemplateView():
    template_name = 'template.html'
    title = 'title'

    def get_context_data(self):
        return {}

    def get_template(self):
        return self.template_name

    def render_template_with_context(self):
        template_name = self.get_template()
        context = self.get_context_data()
        context['title'] = self.title
        return '200 OK', render(template_name, **context)

    def __call__(self, request):
        return self.render_template_with_context()


class ListView(TemplateView):
    queryset = {}
    template_name = 'list.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return self.queryset

    def get_context_object_name(self):
        return self.context_object_name

    def get_context_data(self):
        queryset = self.get_queryset()
        context_object_name = self.get_context_object_name()
        context = {context_object_name: queryset, 'title': self.title}
        return context


class CreateView(TemplateView):
    template_name = 'create.html'

    @staticmethod
    def get_request_data(request):
        return request['request_data']

    def create_obj(self, data):
        pass

    def __call__(self, request):
        if request['method'] == 'post':
            data = self.get_request_data(request)
            self.create_obj(data)

            return self.render_template_with_context()
        else:
            return super().__call__(request)


class Observer:
    def update(self, subject):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def notify(self):
        for item in self.observers:
            item.update(self)


class SMS_Notifier(Observer):
    def update(self, subject):
        text = f'SMS: Student {subject.students[-1].name} was added on {subject.name} course'
        print(f'{"=" * len(text)}\n{text}\n{"=" * len(text)}')


class EMAIL_Notifier(Observer):
    def update(self, subject):
        text = f'EMAIL: Student {subject.students[-1].name} was added on {subject.name} course'
        print(f'{text}\n{"=" * len(text)}')
