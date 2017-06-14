from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=20, help_text='Enter valid name')
    description = models.TextField(max_length=100, help_text='Enter valid description')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('albums:album_detail', args=[str(self.id)])
