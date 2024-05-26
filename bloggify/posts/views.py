from django.shortcuts import render
from posts.models import Post

# Create your views here.
def home_view(request):
    return render(request, 'home.html', 
    {'posts': Post.objects.all().order_by('-date')})