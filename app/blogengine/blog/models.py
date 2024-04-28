from django.db import models
from django.shortcuts import reverse

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

class Post(models.Model):
     title = models.CharField(max_length = 150, db_index = True)
     slug = models.SlugField(max_length = 150, unique = True)
     bodu = models.TextField(blank = True, db_index = True)
     date_pub = models.DateTimeField(auto_now_add = True)


     def get_absolute_url(self):
         return reverse("post_detail_url", kwargs={'slug':self.slug})
     

     def __str__(self):
          return '{}'.format(self.title)
