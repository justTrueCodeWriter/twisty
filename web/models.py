from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default="Linus")


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    text = models.CharField(max_length=281)  # Twitter - suck, with 280 characters

