from django.http import HttpResponse

def home_view(request):
    response = HttpResponse("<h1>Welcome to django</h1>")
    return response
