from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import *

def account(request):
    return render(request, 'users/account.html')

def sign_up(request):
    city_list = City.objects.all().order_by('name')
    hobby_list = Hobby.objects.all().order_by('name')
    if request.method == 'POST':
        form = UserRegistrationForm(data = {'last_name': request.POST.get('last_name'),
                                            'first_name': request.POST.get('first_name'),
                                            'patronymic': request.POST.get('patronymic'),
                                            'city': City.objects.get(name = request.POST.get('city')),
                                            'email': request.POST.get('email'),
                                            'tel': request.POST.get('tel'),
                                            'dob': request.POST.get('dob'),
                                            'username': request.POST.get('username'),
                                            'password1': request.POST.get('password1'),
                                            'password2': request.POST.get('password2')})
      
        if form.is_valid():
            form.save()
            user = User.objects.get(username = request.POST.get('username'))
            hobbys = request.POST.getlist('hobbys')
            for hobby in hobbys:
                user.hobbys.add(Hobby.objects.get(name = hobby))
                user.hobbys.add(request.user.id)
            auth.login(request, user)
            return redirect('/users/account')
    else:
        form = UserRegistrationForm()
    print(1)
    print(city_list) 
    print(hobby_list)
    return render(request, 'users/sign_up.html',{
        'form': form,
        'city_list': city_list,
        'hobby_list': hobby_list,
    })


def sign_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('/user/account/')
    else:
        form = UserLoginForm()
    return render(request, 'users/sign_in.html', {
        'form': UserLoginForm(),
    })


def sign_out(request):
    auth.logout(request)
    return redirect('/')



 