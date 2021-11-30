from django.shortcuts import redirect, render
#from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_user, allowed_users
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home/home.html')

@unauthenticated_user
def register(request):
    
    form = SignUpForm()
    if(request.method == 'POST'):
        form = SignUpForm(request.POST)
    
        if(form.is_valid()):
            user = form.save()

            group = Group.objects.get(name='visitor')

            user.groups.add(group)
            messages.success(request, 'User '+request.POST.get('first_name')+ ' created!')
            return redirect('/login')
        else:
            print('aaaaaaaaaaaaaaaaaaaaaaa')
            messages.warning(request, 'fields filled incorrectly')
            return redirect('/register')
    context = {'form': form}
    return render(request,'home/register.html', context)


@unauthenticated_user
def loginPage(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if(user is not None):
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "username or password incorrect")
            return redirect('login')

    else:

        return render(request, 'home/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@allowed_users(allowed_roles=['dev'])
def todo(request):
    return render(request, 'home/todo.html')

def about(request):
    dt = datetime.today()
    datetime1 = datetime(dt.year, dt.month, dt.day)
    datetime2 = datetime(1998, 5, 15)
    time_difference = relativedelta(datetime1, datetime2)
    age = time_difference.years

    return render(request, 'home/about.html', {'age':age})


def projects(request):
    return render(request, 'home/projects.html')