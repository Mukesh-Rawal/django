from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_us_view(request):
    return render(request, 'aboutus.html')