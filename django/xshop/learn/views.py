from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return  HttpResponse(u"learn index django学习haha")

