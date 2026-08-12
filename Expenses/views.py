from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreation, MainExpenses
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from . models import expenses
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register_form(request):
    if request.method=="POST":
        form=CustomUserCreation(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form=CustomUserCreation()
        
    return render(request, 'registration/register.html', {'form':form})


@login_required
def dashboard(request):     
    all_expenses=expenses.objects.filter(user=request.user)
    return render(request, 'maindashboard.html', {'expenses':all_expenses})

@login_required
def add_expenses(request):
    if request.method=="POST":
        form=MainExpenses(request.POST)
        if form.is_valid():
            user_profile=form.save(commit=False)
            user_profile.user=request.user
            user_profile.save()
            return redirect('dashboard')
    else:
        form=MainExpenses()
        
    return render(request, 'saveExpenses.html', {'form':form})


def update_expenses(request, pk):
    expenses_details=get_object_or_404(expenses, id=pk)
    if request.method=="POST":
        form=MainExpenses(request.POST, instance=expenses_details)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
            
    else:
        form=MainExpenses(instance=expenses_details)
    return render(request, 'saveExpenses.html', {'form':form})

@login_required
def total_expenses(request):
    total=expenses.objects.filter(user=request.user).aggregate(
        Sum('amount')
        
    )['amount__sum'] or 0
    return render(request, 'totalexpenses.html', {'total':total})


def delete_expenses(request, pk):
    expenses_details=get_object_or_404(expenses, id=pk)
    if request.method=="POST":
        expenses_details.delete()
        return redirect('dashboard')
    return render(request, 'confirm.html', {'form':expenses_details})
