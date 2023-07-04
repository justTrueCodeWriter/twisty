from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User,
                                 on_delete=models.CASCADE,
                                 primary_key=True)
    name = models.CharField(max_length=32, default="Linus")

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Profile,
                               on_delete=models.PROTECT)
    text = models.CharField(max_length=281)  # Twitter - suck, with 280 characters

    def __str__(self):
        return self.text[:20]



