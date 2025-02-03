from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Teste Home')
    return render(request, 'home.html')

# def sobre(request):
#     return HttpResponse("Teste Sobre")