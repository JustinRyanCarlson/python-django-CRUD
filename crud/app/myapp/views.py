from django.shortcuts import render
from django.http import HttpResponse
from .models import Snippet


# Create your views here.
def home(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'myapp/home.html.djt', context)


def create(request):
    if request.method == 'POST':
        Snippet(
            title=request.POST['title'],
            description=request.POST['description'],
            snippet=request.POST['snippet'],
            lang=request.POST['lang']
        ).save()

    return render(request, 'myapp/create.html.djt', {})
