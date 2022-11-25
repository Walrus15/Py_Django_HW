from django.contrib import admin
from .models import Author, Book, \
    AuthorTwo, BookTwo, UserTwo, Availability, \
    UserThree, Article, Comment, LikeComment, LikeArticle

admin.site.register(Author)
admin.site.register(Book)

admin.site.register(AuthorTwo)
admin.site.register(BookTwo)
admin.site.register(UserTwo)
admin.site.register(Availability)

admin.site.register(UserThree)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(LikeComment)
admin.site.register(LikeArticle)


