from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=100)
    sbranch = models.CharField(max_length=100)

    def __str__(self):
        return self.sname