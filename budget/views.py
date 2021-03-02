from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import *


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

def expense_create(request):
    form  = ExpenseCreateForm(initial={'user':request.user})
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = ExpenseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addexpense')
    return render(request,'budget/addExpense.html',context)

def view_expense(request):
    form = DateSearchForm()

    context = {}
    expenses = Expense.objects.filter(user=request.user)
    context['form'] = form
    context['expenses'] = expenses
    if request.method=='POST':
        form = DateSearchForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            expenses = Expense.objects.filter(data=date,user=request.user)
            context['expenses'] = expenses
            return render(request, 'budget/viewExpense.html', context)

    return render(request,'budget/viewExpense.html',context)

def edit_expense(request,id):
    id = Expense.objects.get(id=id)
    form = ExpenseCreateForm(instance=id)
    context = {}
    context['form'] = form
    if request.method=='POST':
        form = ExpenseCreateForm(request.POST,instance=id)
        if form.is_valid():
            form.save()
            return redirect('viewexpense')
        else:
            form = ExpenseCreateForm(request.POST,instance=id)
            context = {}
            context['form'] = form
            return render(request,'budget/expenseEdit.html',context)

    return render(request,'budget/expenseEdit.html',context)

def delete_expense(request,id):
    id = Expense.objects.get(id=id)
    id.delete()
    return redirect('viewexpense')
