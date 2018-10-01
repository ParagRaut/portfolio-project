from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(blank=False, max_length=200)


    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __unicode__(self):
        pass

    def __str__(self):
        return(self.summary)
