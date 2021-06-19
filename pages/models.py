from django.db import models


class Photos(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.photo.name



