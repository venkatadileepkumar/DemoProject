from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    return HttpResponse("<h2>***Hello User....!!!This is DemoApp1-f1()***</h2><hr/>");
def f2(request):
    return HttpResponse("<h2>***Hello User....!!!This is DemoApp1-f2()***</h2><hr/>");
