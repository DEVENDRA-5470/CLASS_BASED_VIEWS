from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    country = models.CharField(max_length=255)  

    # Technology choices
    technologies=models.CharField(max_length=200,null=True)

    # Identification choices
    identification = models.CharField(max_length=20,null=True)
    

    date = models.CharField(max_length=20,null=True)
    time = models.CharField(max_length=20,null=True)

    # Address details
    area = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    post_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    stu_name=models.CharField(max_length=20)
    stu_age=models.IntegerField()
    stu_class=models.CharField(max_length=23)