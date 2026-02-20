from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    fathers_name = models.TextField(default='Rahim')

    def __str__(self):
        return f"Roll - {self.roll} -- {self.name}"
    
class StudentModel(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    fathers_name = models.CharField(max_length=40)

    def __str__(self):
        return f'Name: {self.name}'