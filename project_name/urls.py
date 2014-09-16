# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# Default
urlpatterns = patterns('',
    # Admin
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Must have vendors
    (r'^ckeditor/', include('ckeditor.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    from django.views.generic import TemplateView

    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),

        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

        url(r'^404/$', TemplateView.as_view(template_name='404.html')),
        url(r'^500/$', TemplateView.as_view(template_name='500.html')),
    )

# Apps
urlpatterns += patterns('',
    (r'^ckeditor/', include('ckeditor.urls')),
)
