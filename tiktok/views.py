from rest_framework import viewsets
from .serializers import UserSerializer, VideoSerializer
from django.contrib.auth.models import User
from .models import Video

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
