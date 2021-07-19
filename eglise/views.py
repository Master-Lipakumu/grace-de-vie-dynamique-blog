from django.shortcuts import render
from django.views.generic import TemplateView

def Error404View(request,exception):
    return render(request,"404.html", status=404)

def Error403View(request,exception):
    return render(request,"403.html", status=403)

def Error400View(request,exception):
    return render(request,"400.html", status=400)

def Error500View(request):
    return render(request,"500.html", status=500)