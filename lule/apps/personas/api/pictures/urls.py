
from django.urls import path

# Views
from apps.personas.api.pictures.views import *

app_name = 'api_pictures'

urlpatterns = [

    path('1.0/photo/', PhotoListAPI.as_view(), name='user_list_api'),
    path('1.0/photo/<int:pk>/', PhotoDetailAPI.as_view(), name='photo_detail_api'),
]