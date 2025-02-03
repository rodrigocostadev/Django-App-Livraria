
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# def teste(request):
#     return HttpResponse('Hello World')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('livraria.urls')), # Pega o arquivo URLS.py da pasta do app livraria
    # path('teste/',teste),
]
