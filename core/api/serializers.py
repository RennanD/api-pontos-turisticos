from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from localizacao.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):

	
	avaliacoes = AvaliacaoSerializer(many=True)
	endereco = EnderecoSerializer()

	class Meta:
		model = PontoTuristico
		fields = ('id','nome','imagem','avaliacoes','endereco')

class AddSerializer(ModelSerializer):

	
	avaliacoes = AvaliacaoSerializer(many=True)
	endereco = EnderecoSerializer()

	class Meta:
		model = PontoTuristico
		fields = ('id','nome','imagem','desc','endereco')


class DetailSerializer(ModelSerializer):

	atracoes = AtracoesSerializer(many=True)
	endereco = EnderecoSerializer()
	comentarios = ComentarioSerializer(many=True)
	avaliacoes = AvaliacaoSerializer(many=True)


	class Meta:
		model = PontoTuristico
		fields = ('id','nome','desc','aprovado', 'imagem','atracoes','comentarios','avaliacoes','endereco')
