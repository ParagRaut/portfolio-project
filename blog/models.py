from django.db import models

import datetime

# Create your models here.

class Blog(models.Model):
    title = models.CharField(blank=False, max_length=200)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    body = models.TextField(blank=False)
    image = models.ImageField(upload_to="images/")


    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __unicode__(self):
        pass
