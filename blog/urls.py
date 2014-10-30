from django.conf.urls import patterns, include, url
from django.contrib import admin
from posts.views.post_view import ListPosts
from posts.urls import urlpatterns as posts_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
) + posts_urls