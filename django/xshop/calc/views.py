from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.

def add(request,num1=None,num2=None):

    if (num1 != None and num2 != None) == False:
        num1 = request.GET.get("num1")
        num2 = request.GET.get("num2")

    if(num1 == None):
        result = "num1不能为空";
    elif num2 == None:
        result = "num2不能为空"
    else:
        result = str( int(num1) + int(num2) )

    return HttpResponse( result );