from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=130)
    age = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

