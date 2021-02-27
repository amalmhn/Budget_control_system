from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

#registration
def registration(request):
    form = UserRegistrationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('user created')
            return redirect('signin')
        else:
            context['form'] = form
            return render(request,'budget/registration.html',context)
    return render(request,'budget/registration.html',context)
#test test test test@123 django@123
#login
def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwrd = request.POST.get('password')
        #authenticate user  with this uname and password
        #user model has authentication fnctn
        user = authenticate(username=uname,password=pwrd)
        if user is not None:
            login(request,user)
            return render(request,'budget/home.html')
        else:
            
            return render(request, 'budget/login.html',{'message':'Invalid Credentials'})
    return render(request,'budget/login.html')
#logout
def signout(request):
    logout(request)
    return redirect('signin')

