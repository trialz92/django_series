from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("ini halaman product")

def detail(request):
    return HttpResponse("ini halaman detail product")