from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracoesSerializer
from django_filters import rest_framework as filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class AtracaoFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name="nome", lookup_expr='icontains')
    desc = filters.CharFilter(field_name="desc", lookup_expr='icontains')
 
class Meta:
    model = Atracao
    fields = ['nome','desc']

class AtracoesViewSet(ModelViewSet):
    
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    filterset_class = AtracaoFilter