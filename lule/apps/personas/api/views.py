# Rest frameworks
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

# Django
from django.shortcuts import get_object_or_404

# Models
from django.contrib.auth.models import User

# Serializers
from apps.personas.api.serializers import UserSerializer


class UserListAPI(APIView):

    def get(self, request):
        paginator = PageNumberPagination()
        user = User.objects.all()
        paginator.paginate_queryset(user, request)
        serializers = UserSerializer(user, many=True)
        serializer_data = serializers.data
        return paginator.get_paginated_response(serializer_data)

    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializers = UserSerializer(user)
        return Response(serializers.data)

    def put(self, request, pk, formatter=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

