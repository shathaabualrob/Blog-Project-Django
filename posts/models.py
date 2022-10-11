from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Category(models.Model):
    catName = models.CharField(max_length = 20)
    catDesc = models.TextField()
    def __str__(self):
        return self.title
class Post(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

    
class Comment(models.Model):
    text = models.TextField()
    cdate = models.DateField(auto_now = False)
    visible = models.BooleanField()
    def __str__(self):
        return self.title
    
