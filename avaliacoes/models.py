from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Avaliacao(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	avaliacao = models.TextField(null = True, blank = True)
	nota = models.DecimalField(max_digits = 2, decimal_places = 1)
	data = models.DateTimeField(auto_now_add = True)
	

	def __str__(self):
		return self.user.username