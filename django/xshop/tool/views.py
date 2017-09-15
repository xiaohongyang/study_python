from django.shortcuts import render
from django.http import response, request
from django import forms

message = "";
class AddForm(forms.Form):
    num01 = forms.IntegerField(label="数字1")
    num02 = forms.IntegerField(label="数字2")

# Create your views here.
def add(request):

    form = AddForm()
    result = None
    if request.method == 'POST':
        result = {'data' : getAddResult(request),'message' : getMessage()}

    #return render(request, 'add.html',{'result':result})
    return render(request, 'add_form.html',{'result':result,'form':form})

def getAddResult(request):

    global message
    num01 = request.POST.get('num01')
    num02 = request.POST.get('num02')
    if num01==None or num02==None:
        result = False;
        setMessage("数据不正确")
    else:
        result = int(num01) + int(num02)
    return result;

def setMessage(value):
    global  message
    message = value
def getMessage():
    global message
    return message