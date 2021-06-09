from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=20, blank=False, null=False)
    image = models.ImageField()
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.text


