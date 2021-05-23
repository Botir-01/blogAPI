from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly
from . import models
from .serializers import PostSerializer, UserSerializer
# Create your views here.

# class PostList(generics.ListCreateAPIView):
#     #permission_classes = (permissions.IsAuthenticated,)
#     queryset = models.Post.objects.all()
#     serializer_class = PostSerializer
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = models.Post.objects.all()
#     serializer_class = PostSerializer
#
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer