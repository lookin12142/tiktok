from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    url_video = models.URLField(max_length=200)
    duracion = models.DurationField()

    def __str__(self):
        return self.titulo
