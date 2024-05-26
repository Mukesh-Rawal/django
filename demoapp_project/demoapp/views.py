from django.http import HttpResponse

def home_view(request):
    response = HttpResponse("<h1>My first app</h1>")
    return response