import datetime
from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    title = models.CharField(max_length=255)
    date = models.DateField()

    def created_at(self):
        date = self.date.split('-')
        datetime_now = datetime.datetime.now()
        now = datetime.date(datetime_now.year, datetime_now.month, datetime_now.day)
        days_passed = now - datetime.date(int(date[0]), int(date[1]), int(date[2]))
        if days_passed.days == 1:
            return 'created 1 day ago'
        return 'created %s days ago' % days_passed.days