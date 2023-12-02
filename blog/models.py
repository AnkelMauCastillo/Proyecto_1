from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=14, unique=True, default='978-1548476434')
    edicion = models.CharField(max_length=4)

    objects = models.Manager()
    libros = PostManager()

    class Meta:
        ordering = ('-ISBN',)

    def __str__(self):
        return (self.titulo)       
    
    def get_absolute_url(self):
        return reverse('blog:post_detalle',
                       args=[self.ISBN])