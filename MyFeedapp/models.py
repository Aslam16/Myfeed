from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=50,null=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=700,null=True)
    url = models.URLField()
    urlToImage = models.URLField(null=True)
    publishedAt = models.CharField(max_length=20,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Source(models.Model):

    id = models.CharField(max_length=40,primary_key=True)
    name = models.CharField(max_length=50)
    article = models.OneToOneField(Article,on_delete=models.DO_NOTHING)
