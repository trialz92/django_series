from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def detail(request):
    context = {
        "nama_produk" : "Baju Tshirt",
        "varian" : ["merah", "biru", "hijau"]
    }
    return render(request, 'detail.html', context)

def contoh(request):
    return HttpResponse("contoh halaman")