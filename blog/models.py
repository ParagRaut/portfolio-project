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

    def summary(self):
        return self.body[:150]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return(self.title)
