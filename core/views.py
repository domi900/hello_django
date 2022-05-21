from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome):
    return HttpResponse('<h1>Hello {}</h1>' .format(nome))

def soma(request, i, j):
    return HttpResponse('<h1>Soma: {}</h1>' .format(i+j))

def mult(request, i, j):
    return HttpResponse('<h1>Multiplicação: {}</h1>' .format(i*j))