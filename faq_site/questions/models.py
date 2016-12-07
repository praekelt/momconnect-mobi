from django.db import models


class Catagory(models.Model):
    catagory_title = models.CharField(max_length=250)
    catagory_logo = models.FileField()

    def __str__(self):
        return catagory_title
