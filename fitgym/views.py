from django.contrib import messages
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

# Home
def home(request):
    return render(request, 'home.html')

# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("Check username/password"))
            return redirect('login')

    else:
        return render(request, 'login.html')

# Register
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("REGISTER SUCCESSFULLY ! "))
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'forms': form}
    return render(request, 'register.html', context)

# Logout
def logout_user(request):
    logout(request)
    return redirect('home')

# Dashboard
@login_required(login_url='login')
def dashboard(request):
    current_user = request.user
    tasks = Task.objects.filter(user_id=current_user.id).all().order_by('-due_date')
    totalTasksCompleted = Task.objects.filter(done=1).count()
    totalTasksPending = Task.objects.filter(done=0).count()
    context = {
        'tasks': tasks,
        'totalTasksCompleted': totalTasksCompleted,
        'totalTasksPending': totalTasksPending
    }

    return render(request, 'dashboard/home.html', context)

# Delete task
def delete_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        messages.success(request, ("Task deleted successfully!"))
        
    return redirect('dashboard')

# Create task view
def create_task(request):
    return render(request, 'dashboard/create-task.html')

# Register task
def register_task(request):
    user_id = request.user.id
    title = request.POST['title']
    due_date = request.POST['due_date']

    Task.objects.create(user_id=user_id,title=title,due_date=due_date)
    messages.success(request, ("Task created successfully!"))
    return redirect('dashboard')

# Complete task
def complete_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.done = 1
        task.save()
        messages.success(request, ("Task completed successfully!"))

    return redirect('dashboard')

# Edit task
def edit_task(request, id):
    task = Task.objects.get(id=id)
    due_date_formatted = task.due_date.strftime("%Y-%m-%d")

    context = {
        'task': task,
        'title': task.title,
        'due_date': due_date_formatted,
    }

    return render(request, 'dashboard/edit-task.html', context)

# Update task
def update_task(request, id):
    title = request.POST['title']
    due_date = request.POST['due_date']

    Task.objects.filter(id=id).update(title=title,due_date=due_date)
    messages.success(request, ("Task updated successfully!"))
    return redirect('dashboard')

# 404
def error_404_view(request, exception):
    return render(request, '404.html')
