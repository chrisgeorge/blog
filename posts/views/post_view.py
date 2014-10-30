from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from posts.models.post import Post


class ListPosts(ListView):
    template_name = 'index.html'
    model = Post

    def get(self, *args, **kwargs):
        return super(ListPosts, self).get(*args, **kwargs)
