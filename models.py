from django.db import models

from django.contrib.auth.models import User


from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length= 20)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_name
    