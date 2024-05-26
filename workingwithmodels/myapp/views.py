from django.shortcuts import render
from myapp.models import Person
# Create your views here.
def home_view(request):
    return render(request, 'home.html', {'persons':Person.objects.all()})