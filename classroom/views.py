from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import SelectRoleForm
from django.template import RequestContext

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    users = User.objects.all()
    profiles = Profile.objects.all()
    current_user = request.user

    if request.user.is_authenticated:
        try:
            if current_user:
                id =  current_user.id
                user = Profile.objects.get(user_id=id)
                user_role = user.role
                if user_role == 'Student':
                    return render(request, 'student.html', locals())
                elif user_role == 'Teacher':
                    return render(request, 'teacher.html', locals())
                elif user_role == 'Admin':
                    return render(request, 'admin.html', locals())
                else:
                    return redirect('index')
        except:
            return render(request, 'index.html')

    return render(request, 'index.html', locals())

def setprofile(request):
    current_user = request.user
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SelectRoleForm(request.POST)
            if form.is_valid():
                role = form.save(commit=False)
                role.user = current_user
                role.save()

                user_role = form.cleaned_data.get('role')
                if user_role == 'Student':
                    return render(request, 'student.html')
                elif user_role == 'Teacher':
                    return render(request, 'teacher.html')
                elif user_role == 'Admin':
                    return render(request, 'admin.html')
                else:
                    return redirect('index')
        else:
            form = SelectRoleForm()
            return render(request, 'setprofile.html', locals())

@login_required(login_url='/accounts/login/')
def student(request):
    users = User.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'student.html', locals())

@login_required(login_url='/accounts/login/')
def teacher(request):
    users = User.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'teacher.html', locals())

@login_required(login_url='/accounts/login/')
def administrator(request):
    users = User.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'admin.html', locals())
