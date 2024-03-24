from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Expense
from django.contrib.auth.models import User
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
     return render(request, 'main/add_expenses.html')

def edit_expenses(request,pk):
    pass


def delete_expenses(request,pk):
    pass