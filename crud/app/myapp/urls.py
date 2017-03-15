from django.conf.urls import url
from . import views

app_name = "snippets"
urlpatterns = [
    url(r'^read/$', views.read, name='read'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/(?P<snippet_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^update/(?P<snippet_id>[0-9]+)/$', views.update, name='update')
]
