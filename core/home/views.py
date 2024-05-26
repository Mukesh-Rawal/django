from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>hello this is django programming</h1>")

def data(request):
    peoples=[
        {'name':'Mukesh', 'age':'25'},
        {'name':'Rahul', 'age':'23'},
        {'name':'Manish', 'age':'24'},
    ]
    return render(request, 'home.html', context= {'peoples': peoples})