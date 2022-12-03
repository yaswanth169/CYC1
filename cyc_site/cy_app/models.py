from django.db import models

# Create your models here.
# class Members(models.Model):
#     fname=models.CharField(max_length=50)
#     lname=models.CharField(max_length=50)
#
#

class Responseneed(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)

class Responseneed1(models.Model):
    fname=models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    passwo=models.CharField(max_length=50)
