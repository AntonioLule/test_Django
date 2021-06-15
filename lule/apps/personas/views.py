from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from apps.personas.models import Photo

PUBLIC = 'PUB'


class PhotoQueryset(object):

    def get_photos_queryset(self, request):
        if not request.user.is_authenticated():
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        return photos