from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Models
from apps.personas.models import Photo

# Serializer
from apps.personas.api.pictures.serializers import PhotoSerializer, PhotoListSerializer

# Queriset
from apps.personas.views import PhotoQueryset

"""class PhotoListAPI(APIView):

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)"""


class PhotoListAPI(PhotoQueryset, ListCreateAPIView):

    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)  # El metodo get lo dejara pasar pero al post debe estar auteticado

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer  # Segun el metodo ejecutado sera el serializador a utilizar

    def get_queryset(self):
        return self.get_photos_queryset(self.request) # Dependiendo que tipo de usuario sera las fotos que le regrese


class PhotoDetailAPI(PhotoQueryset, RetrieveUpdateDestroyAPIView):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # El metodo get lo dejara pasar pero al post debe estar auteticado

    def get_queryset(self):
        return self.get_photos_queryset(self.request) # Dependiendo que tipo de usuario sera las fotos que le regrese