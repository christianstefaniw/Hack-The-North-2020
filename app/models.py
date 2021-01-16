from django.db import models


class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    caption = models.CharField(max_length=80)
    image = models.ImageField()
    likes = models.ManyToManyField('User', related_name='likes', blank=True)

    def __str__(self):
        return str(self.id)


class User(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return str(self.id)
