from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer,DetailSerializer,AddSerializer
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class AddViewSet(ModelViewSet):

    serializer_class = AddSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        
        queryset = PontoTuristico.objects.all()    

        return queryset


class DetailViewSet(ModelViewSet):

    serializer_class = DetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        
        queryset = PontoTuristico.objects.all()    

        return queryset
        


 


class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'desc','endereco__rua')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        
        queryset = PontoTuristico.objects.all()    

        return queryset

    def list(self, request, *args, **kwargs):
    	return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):

    	return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
    	
    	return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrive(self, request, *args, **kwargs):
    	
    	return super(PontoTuristicoViewSet, self).retrive(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
    	
    	return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
    	
    	return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods = ['post','get'], detail = True)
    def denunciar(self, request, pk=None):
    	
    	return Response({'msg': "denunciou"})

    @action(methods = ['get'], detail = False)
    def teste(self, request):
    	
    	return Response({'msg': "denunciou"})