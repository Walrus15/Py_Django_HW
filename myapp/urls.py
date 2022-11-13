from django.urls import path, re_path
from .views import articles, articles_archive, \
    users, articles_num, articles_archive_num, \
    users_num, regular, number_phone, index, first

urlpatterns = [
    path('first/', first, name='first'),
    path('articles/', articles),
    path('articles/archive/', articles_archive),
    path('users/', users),
    path('articles/<int:article_number>', articles_num),
    path('articles/<int:article_number>/<slug:slug_text>', articles_archive_num, name='temp1'),
    path('users/<int:article_number>', users_num),


    re_path('[1-9a-f]{4}-[1-9a-f]{6}', regular),
    re_path('articles/[+][0-9]{10,14}', number_phone),
]