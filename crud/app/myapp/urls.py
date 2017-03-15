from django.conf.urls import url
from . import views

app_name = "snippets"
urlpatterns = [
    # ^ means start of the line                   ie home2595438509284059820    works
    # $ means it should be the end of the line    ie /home/                     works
    url(r'^read/$', views.read, name='read'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/(?P<snippet_id>[0-9]+)/$', views.delete, name='delete')
]
