from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Endereco
# Create your models here.

class PontoTuristico(models.Model):
	nome = models.CharField(max_length = 250)
	desc = models.TextField()
	aprovado = models.BooleanField(default = True)
	atracoes = models.ManyToManyField(Atracao)
	comentarios = models.ManyToManyField(Comentario,null = True, blank = True)
	avaliacoes = models.ManyToManyField(Avaliacao,null = True, blank = True)
	endereco = models.ForeignKey(Endereco, on_delete = models.CASCADE,null = True, blank = True)
	imagem = models.ImageField(upload_to = 'pontosturisticos',null = True, blank = True)


	def __str__(self):

		return self.nome
		