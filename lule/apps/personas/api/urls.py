from django.urls import path

# Views
from apps.personas.api.views import *

app_name = 'api_personas'

urlpatterns = [

    path('1.0/users/', UserListAPI.as_view(), name='user_list_api'),
    path('1.0/users/<int:pk>/', UserDetailAPI.as_view(), name='user_detail_api'),
]