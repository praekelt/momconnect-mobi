from django.db import models


class Catagory(models.Model):
    catagory_title = models.CharField(max_length=250)
    catagory_logo = models.FileField()

    def __str__(self):
        return self.catagory_title


class QandA(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=2000)

    def __str__(self):
        return self.question
