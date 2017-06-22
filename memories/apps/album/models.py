from django.db import models
from django.conf import settings
from django.urls import reverse
from .managers import AlbumManager

def uploader_path(instance, file_name):
    return '{0}/{1}/{2}'.format(instance.__class__.__name__.lower(), instance.user.id, file_name)
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=20, help_text='Enter valid name')
    description = models.TextField(max_length=100, help_text='Enter valid description')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, blank = True,
                             related_name = 'albums', verbose_name = 'user')
    image = models.ImageField(upload_to=uploader_path, null=True, blank=True)

    objects = AlbumManager()

    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('albums:album_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Album'
        ordering = ['name']
