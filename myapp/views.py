from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s

def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
        'now': datetime.now(),
    })


def first(request):
    return render(request, 'first.html')

def articles(request):
    return HttpResponse("http://127.0.0.1:8000/articles")

def articles_archive(request):
    return HttpResponse("http://127.0.0.1:8000/articles/archive")

def users(request):
    return HttpResponse("http://127.0.0.1:8000/users")

def articles_num(request, article_number):
    article_number = article_number
    return render(request, 'temp1.html', {
        'article_number': article_number,
    })

def articles_archive_num(request, article_number, slug_text):
    article_number = article_number
    slug_text = slug_text
    return render(request, 'temp1.html', {
        'slug_text': slug_text,
        'article_number': article_number,
    })

def users_num(request, article_number):
    return HttpResponse("http://127.0.0.1:8000/users/int:user_number>")

def regular(request):
    return HttpResponse("Regular Viragenie Good")

def number_phone(request):
    return HttpResponse('number good')
