from django.db import models

# Create your models here.
gender_choices=(('Male','Male'),
                ('Female','Female'),
                ('Others','Others'))
class Register(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    age=models.PositiveIntegerField()
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=250)
    mobile=models.IntegerField()
    gender=models.CharField(max_length=10,choices=gender_choices)
    def __str__(self) -> str:
        return self.firstname
