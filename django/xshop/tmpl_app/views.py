from json import dumps

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def abount(request):

    tutoriaList = ["php","python","js",'c#','java']
    infoDisc = {"desc":"肖红阳的python网站","title":"Python学习网","key":"Python 学习"}

    return  render(request, "about.html", {'tutoriaList' : tutoriaList, "infoDisc" : infoDisc, 'infoJson' : dumps(infoDisc)})

def help(request):
    return  render(request, "help.html")