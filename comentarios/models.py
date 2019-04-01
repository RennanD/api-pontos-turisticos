from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Comentario(models.Model):
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)
	comentario = models.TextField()
	data = models.DateTimeField('Created Time',auto_now_add = True)
	aprovado = models.BooleanField(default = True)

	def __str__(self):
		return self.usuario.username