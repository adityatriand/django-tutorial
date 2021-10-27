from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    pengalaman = models.PengalamanBelajar.objects.all()
    context = {
        'judul':'Install Django',
        'belajars': pengalaman
    }
    return render(request, 'belajar/index.html', context)