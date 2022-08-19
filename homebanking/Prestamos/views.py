from django.shortcuts import render

# Create your views here.

def prestamos(request):
    if not (request.user.is_authenticated):
        return render(request, 'ITBA/index.html')

    return render(request, 'Prestamos/prestamos.html')