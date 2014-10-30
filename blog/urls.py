from django.conf.urls import patterns, include, url
from django.contrib import admin
from posts.views import ListPosts

urlpatterns = patterns('',
    url(r'^posts/$', ListPosts.as_view(), name="posts_list"),
    url(r'^admin/', include(admin.site.urls)),
)
