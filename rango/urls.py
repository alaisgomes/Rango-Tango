from django.conf.urls import url
from rango import views
from django.conf import settings

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about')
        ]

if settings.DEBUG:
    urlpatterns += [
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), ]