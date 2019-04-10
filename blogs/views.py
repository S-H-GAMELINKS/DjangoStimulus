from django.shortcuts import render

from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    return render(request, 'index.html')
