from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home2.html', {'msg':'This is my first web page', 'age':[22, 30,32]})

def about_view(request):
    return render(request, 'home1.html', {'names':['Mukesh', 'Mahima', 'pakaj']})