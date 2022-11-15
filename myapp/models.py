from django.db import models


# 1. Каталог
class Author(models.Model):
    name = models.CharField(max_length=59)

class Book(models.Model):
    title = models.CharField(max_length=119)
    date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# 2. Библиотека
class AuthorTwo(models.Model):
    name = models.CharField(max_length=59)
    surname = models.CharField(max_length=59)

    def __str__(self):
        return self.name

class BookTwo(models.Model):
    title = models.CharField(max_length=119)
    date = models.DateField(blank=True)
    author = models.ManyToManyField(AuthorTwo, blank=True)

    def __str__(self):
        return self.title

class UserTwo(models.Model):
    name = models.CharField(max_length=59)
    surname = models.CharField(max_length=59)
    time_take = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Availability(models.Model):
    user = models.ForeignKey(UserTwo, on_delete=models.CASCADE)
    book = models.ForeignKey(BookTwo, on_delete=models.CASCADE)

# 3. Статья
class UserThree(models.Model):
    name = models.CharField(max_length=59)
    surname = models.CharField(max_length=59)

    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(UserThree, on_delete=models.CASCADE)
    title = models.CharField(max_length=59)
    description = models.TextField(max_length=359)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(UserThree, on_delete=models.CASCADE)
    comment = models.TextField(max_length=359)
    com_com = models.ForeignKey('myapp.Comments', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.comment

class LikeComment(models.Model):
    user = models.ForeignKey(UserThree, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

class LikeArticle(models.Model):
    user = models.ForeignKey(UserThree, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)