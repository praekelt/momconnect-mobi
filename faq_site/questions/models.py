from django.db import models


class Catagory(models.Model):
    catagory_title = models.CharField(max_length=250)
    catagory_logo = models.ImageField()

    def __str__(self):
        return self.catagory_title

# QandA's are associated with Catagories and can have a many to one relation


class QandA(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
