from django.shortcuts import render

# Create your views here.
def add_view(request):
    if request.method == 'POST':
        n1 = int(request.POST['firstnum'])
        n2 = int(request.POST['secondnum'])
        sum = n1+n2
        return render(request, 'result.html', {'add':sum})
    else:
        return render(request, 'add.html')
    
def result_view(request):
    return render(request, 'result.html')