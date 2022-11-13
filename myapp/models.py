from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=59)

class Book(models.Model):
    title = models.CharField(max_length=119)
    date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



class Author_two(models.Model):
    name = models.CharField(max_length=59)
    surname = models.CharField(max_length=59)

    def __str__(self):
        return self.name

class User_two(models.Model):
    name = models.CharField(max_length=59)
    surname = models.CharField(max_length=59)
    time_take = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Book_two(models.Model):
    title = models.CharField(max_length=119)
    date = models.DateField(blank=True)
    author = models.ManyToManyField(Author_two, blank=True)
    user = models.ManyToManyField(User_two, blank=True)
    availability = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.title


class Likes(models.Model):
    like = models.BooleanField()

class Comments(models.Model):
    comment = models.TextField(max_length=359)
    like = models.OneToOneField(Likes, on_delete=models.CASCADE, blank=True)
    com_com = models.OneToOneField('myapp.Comments', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.comment

class Articles(models.Model):
    title = models.CharField(max_length=59)
    description = models.TextField(max_length=359)
    comment = models.OneToOneField(Comments, on_delete=models.CASCADE, blank=True)
    like = models.OneToOneField(Likes, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title