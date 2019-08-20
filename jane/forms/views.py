from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Jane

def fillForm(request,form_id):
    context = {
        'id': form_id,
    } 
    return render(request, 'forms/form.html', context)

def index(request):
    janelist = Jane.objects.all()
    context = {
        'janelist': janelist,
    }
    return render(request, 'forms/index.html', context)

def submit(request,form_id):
    firstname = request.POST['first']
    lastname = request.POST['last']
    animal = request.POST['animal']
    favoriteverse = request.POST['verse']
    friend= request.POST['friend']
    j = Jane(first_name=firstname, last_name=lastname, animal=animal, favorite_verse=favoriteverse, friend=friend)
    j.save()
    return HttpResponse(j)

def help(request):
    return HttpResponse("Help")
# Create your views here.
