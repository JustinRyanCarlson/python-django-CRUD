from django.conf.urls import url
from . import views

app_name = "snippets"
urlpatterns = [
    # ^ means start of the line                   ie home2595438509284059820    works
    # $ means it should be the end of the line    ie /home/                     works
    url(r'^home/$', views.home, name='home'),
    url(r'^create/$', views.create, name='create')
]