from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

# Models
from apps.personas.models import Photo

# Serializer
from apps.personas.api.pictures.serializers import PhotoSerializer, PhotoListSerializer

# Queriset
from apps.personas.views import PhotoQueryset


class PhotoListAPI(PhotoQueryset, ListCreateAPIView):

    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)  # El metodo get lo dejara pasar pero al post debe estar auteticado

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer  # Segun el metodo ejecutado sera el serializador a utilizar

    def get_queryset(self):
        return self.get_photos_queryset(self.request) # Dependiendo que tipo de usuario sera las fotos que le regrese

    # TODO: este metodo se ejecuta cuando la peticion es post y le estoy diciando que al guardar el owner siempre sea el usuario autenticado no importando que le manden
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PhotoDetailAPI(PhotoQueryset, RetrieveUpdateDestroyAPIView):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # El metodo get lo dejara pasar pero al post debe estar auteticado

    def get_queryset(self):
        return self.get_photos_queryset(self.request) # Dependiendo que tipo de usuario sera las fotos que le regrese


# Todo: ViewSets proporciona los sigientes metodos: list #GET (listado), create #POST, retrieve #GET(Detalle), update #PUT, partial_update #PATCH, destroy #DELETE
"""
:Esta clase basada en viewsets hace lo mismo que las dos de arriba
"""


class PhotoViewSet(PhotoQueryset, ModelViewSet):

    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
