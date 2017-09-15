from django.shortcuts import render
from django.http import request, HttpResponse
from django.http import response
from .forms import AddForm

# Create your views here.



def index(request):
    return render(request, 'index.html', {'title':'首页'})

def list(request):

    listData = [
        {'title' : '文章1....'},
        {'title' : '文章2....'},
        {'title' : '文章3....'},
        {'title' : '文章4....'},
        {'title' : '文章5....'},
    ];

    listData2 = [
        ('title','文章1'),
        ('title','文章2'),
        ('title','文章3'),
        ('title','文章4'),
    ]

    return  render(request, 'articles.html', {'title':'最新文章', 'listData' : listData, 'listData2' : listData2})

def detail(request):
    return render(request, 'detail.html', {'title':'详情页'})

def add(request):



    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            return HttpResponse('ok')

    return render(request, 'add.html', {'title':'add运算', 'form':form})


def doAdd(request):

    if request.method == 'POST':
        formz = AddForm(request.POST)




        return HttpResponse(str(c))