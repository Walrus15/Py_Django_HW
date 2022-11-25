import random
from myapp.models import Comment

from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
from string import ascii_uppercase
from random import choice




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
    urls = ['first/', 'articles/', 'articles/archive/', 'users/']

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
        'urls': urls,
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


def five_last_comment(request):
    comment = Comment.comment
    comment_five1 = Comment.objects.filter().order_by('pk')[:5]
    return render(request, 'url1.html', {
        'comment': comment,
        'comment_five1': comment_five1,
    })

def different_text(request):
    comment2 = Comment.comment
    comment_five2 = Comment.objects.filter().order_by('pk')[5:10]
    return render(request, 'url2.html', {
        'comment2': comment2,
        'comment_five2': comment_five2,
    })

def date_save(request):
    comment3 = Comment.comment
    comment_five3 = Comment.objects.filter().order_by('pk')[10:11]
    return render(request, 'url3.html', {
        'comment3': comment3,
        'comment_five3': comment_five3,
    })

def update_text(request):
    comment4 = Comment.comment
    Comment.objects.filter(comment__icontains='Start').update(comment='Start hi')
    Comment.objects.filter(comment__icontains='Middle').update(comment='Middle hi')
    Comment.objects.filter(comment__icontains='Finish').update(comment='Finish hi')

    comment_start = Comment.objects.filter(comment__icontains='Start')
    comment_mid = Comment.objects.filter(comment__icontains='Middle')
    comment_finish = Comment.objects.filter(comment__icontains='Finish')
    return render(request, 'url4.html', {
        'comment4': comment4,
        'comment_start': comment_start,
        'comment_mid': comment_mid,
        'comment_finish': comment_finish,
    })

def delete_comments(request):
    comment5 = Comment.comment
    Comment.objects.filter(comment__contains='k').exclude(comment__contains='c').delete()
    comment_delete = Comment.objects.order_by('pk').all()
    return render(request, 'url5.html', {
        'comment5': comment5,
        'comment_delete': comment_delete,
    })

def comment_alfavit(request):
    comment6 = Comment.comment
    comment_alf = Comment.objects.filter(article__date='2022-11-25').order_by('-article__user__name')[:2]
    return render(request, 'url6.html', {
        'comment6': comment6,
        'comment_alf': comment_alf,
    })

