from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

# Views
from apps.personas.api.pictures.views import *

app_name = 'api_pictures'

# APIRouter
router = DefaultRouter()
router.register(r'1.0/photo-viewset', PhotoViewSet)

urlpatterns = [

    #path('1.0/photo/', PhotoListAPI.as_view(), name='user_list_api'),
    #path('1.0/photo/<int:pk>/', PhotoDetailAPI.as_view(), name='photo_detail_api'),

    # TODO: La url del PhotoViewSet ara en una sola lo que hacen las dos de arriva
    path('', include(router.urls))
]

#print(urlpatterns)
