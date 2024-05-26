from django.shortcuts import render, redirect
from mytask.models import Task

# Create your views here.
def add_task_view(request):
    if request.method == 'POST':
        new_task = Task()
        new_task.title = request.POST['title']
        new_task.description = request.POST['description']
        new_task.save()
        print("New task added successfully")
        return redirect('view-tasks')
    else:
        return render(request, 'add.html')
    
def all_task_view(request):
    return render(request, 'view.html', {'tasks':Task.objects.all()})