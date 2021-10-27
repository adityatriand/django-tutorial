from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Install Django'
    }
    return render(request, 'belajar/index.html', context)