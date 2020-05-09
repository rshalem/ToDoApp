from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList
from .forms import ToDoForm


@login_required(login_url="/")
def index(request):

    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['task_title']
            new_task = ToDoList.objects.create(task_title=title, user=request.user)
            new_task.save()
            return redirect('todoapp:homepage')

        messages.info(request, 'Please enter valid parameters')

    form = ToDoForm()

    list = ToDoList.objects.all()

    context = {
        'form': form,
        'list': list
    }

    return render(request, 'index.html', context=context)

def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('todoapp:homepage')

        else:
            messages.info(request, 'Invalid User')
            return redirect('todoapp:login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('todoapp:login')

@login_required(login_url='/')
def complete(request, id):
    task_obj = get_object_or_404(ToDoList, id=id)
    task_obj.complete = True
    task_obj.save()

    return redirect('todoapp:homepage')
