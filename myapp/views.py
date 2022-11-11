from django.shortcuts import render
from django.shortcuts import HttpResponse

def first(request):
    return HttpResponse("Hi")

def articles(request):
    return HttpResponse("http://127.0.0.1:8000/articles")

def articles_archive(request):
    return HttpResponse("http://127.0.0.1:8000/articles/archive")

def users(request):
    return HttpResponse("http://127.0.0.1:8000/users")

def articles_num(request, article_number):
    return HttpResponse("articles/<int:article_number>")

def articles_archive_num(request, article_number, slug_text):
    return HttpResponse("articles/<int:article_number>/<slug:slug_text>")

def users_num(request, article_number):
    return HttpResponse("http://127.0.0.1:8000/users/int:user_number>")

def regular(request):
    return HttpResponse("Regular Viragenie Good")

def number_phone(request):
    return HttpResponse('number good')
