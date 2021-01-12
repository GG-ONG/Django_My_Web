from django.shortcuts import render
from . models import Post
from django.views.generic import ListView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

def post_detail(request, pk):
    blog_post = Post.objects.get(pk=pk)
