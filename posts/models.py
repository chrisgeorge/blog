from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    title = models.CharField(max_length=255)
    date = models.DateField()
