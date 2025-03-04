from django.db import models

# Create your models here.

class Color(models.Model):
    color_name = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.color_name

class Person(models.Model):
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name='color_detail',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=130)
    age = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.name} | {self.created_on.date()}'