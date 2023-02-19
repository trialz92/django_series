from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def detail(request):
    return HttpResponse("ini halaman detail product")

def contoh(request):
    return HttpResponse("contoh halaman")