# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# Default
urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),

    # Must have vendors
    (r'^ckeditor/', include('ckeditor.urls')),
)

# Static
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

# Apps
urlpatterns += patterns('',
)
