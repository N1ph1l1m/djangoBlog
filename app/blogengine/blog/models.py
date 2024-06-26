from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
     new_slug = slugify(s, allow_unicode=True)
     return new_slug + '-' + str(int(time()))


# Create your models here.


class Worker(models.Model):
     name = models.CharField(max_length=150,blank=False)
     second_name = models.CharField(max_length=150,blank=False)
     salary = models.IntegerField(default=0)
     cat_id= models.ForeignKey('Category', on_delete = models.PROTECT, null = True)

     def __str__(self):
          return self.name


class Category(models.Model):
     name = models.CharField(max_length=100, db_index=True)

     def __str__(self):
          return self.name


class Post(models.Model):
     title = models.CharField(max_length = 150, db_index = True)
     slug = models.SlugField(max_length = 150, blank=True, unique = True)
     bodu = models.TextField(blank = True, db_index = True)
     date_pub = models.DateTimeField(auto_now_add = True)
     tags = models.ManyToManyField('Tag', blank=True, related_name='posts')


     def get_absolute_url(self):
         return reverse("post_detail_url", kwargs={'slug':self.slug})

     def save(self, *args, **kwargs):
          if not self.id:
               self.slug = gen_slug(self.title)
          super().save(*args, **kwargs)

     def get_update_url(self):
          return reverse ('post_update_url', kwargs={'slug':self.slug})

     def get_delete_url(self):
          return reverse('post_delete_url', kwargs={'slug':self.slug})


     def __str__(self):
          return self.title

     class Meta:
          ordering = ['-date_pub']

class Tag(models.Model):
     title = models.CharField(max_length=50)
     slug = models.SlugField(max_length=50, blank=True ,  unique = True)


     def save(self, *args, **kwargs):
          if not self.id:
               self.slug = gen_slug(self.title)
          super().save(*args, **kwargs)

     def get_absolute_url(self):
          return reverse('tag_detail_url', kwargs = {'slug':self.slug})

     def get_delete_url(self):
          return reverse('tag_delete_url', kwargs={'slug':self.slug})

     def get_update_url(self):
          return reverse ('tag_update_url', kwargs={'slug':self.slug})

     def __str__(self):
          return  self.title

     class Meta:
          ordering = ['title']
