from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'main/dashboard.html')


def all_expenses(request):
    return render(request, 'main/expenses.html')

def add_expenses(request):
     return render(request, 'main/add_expenses.html')

def edit_expenses(request,pk):
    pass


def delete_expenses(request,pk):
    pass