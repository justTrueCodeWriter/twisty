from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User,
                                 on_delete=models.CASCADE,
                                 primary_key=True)
    name = models.CharField(max_length=32,
                            default="Linus")
    registered = models.DateField(auto_now_add=True,
                                  auto_now=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Profile,
                               on_delete=models.PROTECT)
    text = models.CharField(max_length=281)
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False)
    changed = models.DateTimeField(auto_now=True,
                                   null=True)
    karma = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:20]


class Commentary(models.Model):
    author = models.ForeignKey(Profile,
                               on_delete=models.PROTECT)
    commented_by = models.ForeignKey(Post,
                                     on_delete=models.PROTECT)
    text = models.CharField(max_length=281)
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False)

    def __str__(self):
        return f"{self.author.name} to {self.commented_by.author.name}: {self.text[:20]}"
