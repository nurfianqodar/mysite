from django.shortcuts import render


def index(request):
    context = {
        'HEADER': 'Beranda-Kang Joki :/'
    }
    return render(request, 'home/index.html', context)
