from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Expense
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ExpenseForm
# Create your views here.

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'main/dashboard.html')

@login_required(login_url='login')
def all_expenses(request):
    all_expenses = Expense.objects.filter(owner=request.user)
    context ={"expenses": all_expenses}
    return render(request, 'main/expenses.html', context)

def add_expenses(request):
    
    form = ExpenseForm()
    context ={"form": form}
    
    if request.method == 'GET':
        return render(request, 'main/add_expense.html', context)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.owner = request.user
            data.save()
            
            return redirect("all-expenses")
        
        


def edit_expenses(request,pk):
    expense = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=expense)
    context ={"form": form}
    
    if request.method == 'GET':
        return render(request, 'main/edit_expense.html', context)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.owner = request.user
            data.save()
            
            return redirect("all-expenses")
        
    


def delete_expenses(request,pk):
     expense = Expense.objects.get(id=pk)
     expense.delete()
     
     return redirect("all-expenses")