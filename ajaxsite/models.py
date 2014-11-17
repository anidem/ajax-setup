from django.db import models
from django.core.urlresolvers import reverse

class Observation(models.Model):
    text = models.TextField()

class Comment(models.Model):
    text = models.TextField()
    subject = models.CharField(max_length=48)

    def get_absolute_url(self):
        return reverse('view_comment', args=[self.id])

