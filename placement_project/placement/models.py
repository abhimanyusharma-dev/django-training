from django.db import models


class User(models.Model):

    student_id = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    mobile = models.CharField(
        max_length=15
    )

    branch = models.CharField(
        max_length=100
    )

    password = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.student_id