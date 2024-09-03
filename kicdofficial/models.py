
from django.db import models

class Kicdofficial(models.Model):
    teacher_id = models.PositiveSmallIntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
  

   
