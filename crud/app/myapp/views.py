from django.shortcuts import render
from django.http import HttpResponse
from .models import Snippet


# Create your views here.
def read(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'myapp/read.html.djt', context)


def create(request):
    if request.method == 'POST':
        Snippet(
            title=request.POST['title'],
            description=request.POST['description'],
            snippet=request.POST['snippet'],
            lang=request.POST['lang']
        ).save()

    return render(request, 'myapp/read.html.djt', {})

# def update


def delete(request, snippet_id):
    print(request.method)
    if request.method == 'DELETE':
        return render(request, 'myapp/read.html.djt', {})
