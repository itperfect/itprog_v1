from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('<h4>Проверка работы</h4>')
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football',
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    # return HttpResponse('<h4>Страница про Нас</h4>')
    return render(request, 'main/about.html')
