from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author
from django.http import Http404

# Create your views here.

def index(request):
    return HttpResponse("Anasayfa")

def authors(request):
    context = {
        'authors_list' : Author.objects.all()
    }
    return render(request, 'authors.html',context)

def books(request):
    return HttpResponse("Kitaplar")

def authorDetails(request, authorId):                       # yazar hakkinda detaylar fonksiyonu
    try:
        context = {
            'author_detail' : Author.objects.get(pk=authorId)
        }
    except Author.DoesNotExist:
        raise Http404("Yazar Bulunamadi")                   # burasi bize olusturdugumuz 404 sayfasinin aciklamasini verir404 sayfa

    return render(request, 'authorDetail.html',context)

