from django.conf.urls import patterns, include, url
from posts.views.post_view import ListPosts

urlpatterns = patterns('',
    url(r'^$', ListPosts.as_view(), name="home"),
    url(r'^posts/$', ListPosts.as_view(), name="posts_list"),
)
