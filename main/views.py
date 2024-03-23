from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'main/dashboard.html')


def all_expenses(request):
    pass

def add_expenses(request):
    pass

def edit_expenses(request,pk):
    pass


def delete_expenses(request,pk):
    pass