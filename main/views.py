from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Expense
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ExpenseForm
from django.core.paginator import Paginator
import django_filters
import datetime
from django.http import JsonResponse
import json
# Create your views here.

@login_required(login_url='login')
def dashboard_view(request):
    expenses = Expense.objects.filter(owner=request.user)
    lables = ['Education','Groceries','Transportation','Utilities','Cash','Fixed expenses','Savings contributions',"Shopping"]
    expenses_data =[]
    
    for category in lables:
        total = 0
        for expense in expenses:
            if category == expense.category:
                total += expense.amount
        expenses_data.append(total)
    
    print(expenses_data)
                
            
       

        
    context = {"labels":lables,"data":expenses_data}
    return render(request, 'main/dashboard.html', context)


class ExpenseFilter(django_filters.FilterSet):
 
    class Meta:
        model = Expense
        fields = ['merchant','payment_method']

@login_required(login_url='login')
def all_expenses(request):
    all_expenses = ExpenseFilter(request.GET, queryset=Expense.objects.filter(owner=request.user))
    all_expenses = all_expenses.qs
    
    # adding pagination
    paginator = Paginator(all_expenses,5)
    page_number = request.GET.get('page')
    page_object = Paginator.get_page(paginator,page_number)
    context ={"expenses": page_object}
    return render(request, 'main/expenses.html', context)


@login_required(login_url='login')
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
        
        

@login_required(login_url='login')
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
        
    

@login_required(login_url='login')
def delete_expenses(request,pk):
     expense = Expense.objects.get(id=pk)
     expense.delete()
     
     return redirect("all-expenses")
 
 
 
def expense_category_summary(request):
    today_date = datetime.date.today()
    three_moths_ago = today_date - datetime.timedelta(days=30*6)
    expenses = Expense.objects.filter(owner= request.user, dat__gte=three_moths_ago, date_lte=today_date)
    
    final_rep ={}
    
    def get_category(expense):
        return expense.category
    
    category_list= list(set(map(get_category,expenses)))
    
    def get_category_amount(category):
        amount =0
        filtered_by_category =expenses.filter(category=category)
        for item in filtered_by_category:
            amount += item.amount
        return amount
    
    for x in expenses:
        for y in category_list:
            final_rep[y] = get_category_amount(y)
    
    return JsonResponse({'expense_category_data': final_rep}, safe=False)
    

def analytics(request):
    return render(request, 'main/analytics.html')