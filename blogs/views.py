from django.shortcuts import render
from django.http import Http404
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def show(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExit:
        raise Http404("Post does not exist!")

    return render(request, 'show.html', {'post': post})
