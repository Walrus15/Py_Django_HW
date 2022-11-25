from django.urls import path, re_path
from .views import articles, articles_archive, \
    users, articles_num, articles_archive_num, \
    users_num, regular, number_phone, first, index, \
    five_last_comment, different_text, date_save, update_text, delete_comments, comment_alfavit

urlpatterns = [
    path('first/', first, name='first'),
    path('articles/', articles),
    path('articles/archive/', articles_archive),
    path('users/', users),
    path('articles/<int:article_number>', articles_num),
    path('articles/<int:article_number>/<slug:slug_text>', articles_archive_num, name='temp1'),
    path('users/<int:article_number>', users_num),

    path('url1/', five_last_comment, name='url1'),
    path('url2/', different_text, name='url2'),
    path('url3/', date_save, name='url3'),
    path('url4/', update_text, name='url4'),
    path('url5/', delete_comments, name='url5'),
    path('url6/', comment_alfavit, name='url6'),

    re_path('[1-9a-f]{4}-[1-9a-f]{6}', regular),
    re_path('articles/[+][0-9]{10,14}', number_phone),
]