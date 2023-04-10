from django.http import HttpResponse
from django.shortcuts import render
from .models import Place


def demo(request):
    obt=Place.objects.all()
    return render(request,"index.html",{'result':obt})





# Create your views here.
