from django.shortcuts import render
from django.http import HttpResponse
from .models import Snippet
from django.shortcuts import redirect
from django.http import JsonResponse

# Create your views here.


def read(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'myapp/read.html.djt', context)


def create(request):
    Snippet(
        title=request.POST['title'],
        description=request.POST['description'],
        snippet=request.POST['snippet'],
        lang=request.POST['lang']
    ).save()
    return redirect('/read/')


def update(request, snippet_id):
    if request.method == "GET":
        snippets = Snippet.objects.filter(id=snippet_id)
        context = {'snippets': snippets}
        return render(request, 'myapp/update.html.djt', context)

    elif request.method == "POST":
        Snippet.objects.filter(id=snippet_id).update(
            title=request.POST['title'],
            description=request.POST['description'],
            snippet=request.POST['snippet'],
            lang=request.POST['lang']
        )
        return redirect('/read/')


def delete(request, snippet_id):
    Snippet(id=snippet_id).delete()
    return JsonResponse({'result': 'done'})
