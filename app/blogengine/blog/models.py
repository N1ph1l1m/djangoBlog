from django.db import models

# Create your models here.


class Worker(models.Model):
     name = models.CharField(max_length=150,blank=False)
     second_name = models.CharField(max_length=150,blank=False)
     salary = models.IntegerField(default=0)



class Color_test(models.Model):
     name = models.CharField(max_length=150,blank=False)
     color_typy = models.IntegerField(default=100)


class Color_test2(models.Model):
     name = models.CharField(max_length=150,blank=False)
     color_typy = models.IntegerField(default=100)
     color_typys = models.IntegerField(default=100)
