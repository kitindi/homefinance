from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Expense, Budget
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ExpenseForm,BudgetForm
from django.core.paginator import Paginator
import django_filters
import datetime
from django.http import JsonResponse
import json
from django.db.models import Sum
# Create your views here.

@login_required(login_url='login')
def dashboard_view(request):
    expenses = Expense.objects.filter(owner=request.user)
    budgets = Budget.objects.filter(owner=request.user)
    total_budget = Budget.objects.filter(owner=request.user).aggregate(Sum('amount'))
    total_budget = total_budget['amount__sum']
    lables = ['Education','Groceries','Transportation','Utilities','Fixed expenses',"Shopping"]
    lables_budgets = []
    expenses_data =[]
    mothly_expenses = []
    total_expenses =0
    monthly_savings = []
    expense_percentages = []
    savings_amount = 0
    
    # pagination for expense listings
    paginator = Paginator(expenses,4)
    page_number = request.GET.get('page')
    page_object = Paginator.get_page(paginator,page_number)
  
    
    for category in lables:
        total = 0
        for expense in expenses:
            if category == expense.category:
                total += expense.amount
                print()
        expenses_data.append(total)

# calculate total mothly expense for each month
    for month in range(1,12):
        total = 0
        for expense in expenses:
            if expense.date.month == month:
                 total += round(expense.amount,0)                
        
        mothly_expenses.append(total)  
   
# calculate total mothly expense for each month
    
    for expense in expenses:
        if expense.category != 'Savings contributions':
            total_expenses += round(expense.amount,0)               
        

# calculate total mothly savings for each month
    for month in range(1,12):
        total = 0
        for budget in budgets:
            if budget.date_created.month == month and budget.category == 'Savings contributions':
                savings_amount = budget.amount
                total += round(budget.amount,0)               
        
        monthly_savings.append(total)  
# calculate % of expense to the budget
    for index in range(6):
       for budget in budgets:
           if lables[index] == budget.category:
             cost = expenses_data[index]
             budget_tospend = budget.amount
             lables_budgets.append(budget_tospend)
             percent = round((cost / budget_tospend)*100,0)
             expense_percentages.append(percent)
            
    print(expense_percentages)
    
    balance = total_budget - total_expenses- savings_amount          
    context = {"expenses":page_object,"labels":lables,"data":expenses_data,"expenses_data":mothly_expenses,"savings_data":monthly_savings, "total_expenses":total_expenses,"total_budget":total_budget, 'balance':balance,'education':expense_percentages[0],'edu_budget':lables_budgets[0],'groceries':expense_percentages[1],'grocery_budget':lables_budgets[1],'transportation':expense_percentages[2],'trans_budget':lables_budgets[2],'utilities':expense_percentages[3],'util_budget':lables_budgets[3],'fixed':expense_percentages[4],'fixed_budget':lables_budgets[4],'shoping':expense_percentages[5],'shop_budget':lables_budgets[5]}
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
 
 
@login_required(login_url='login') 
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
    

def budget(request):
    budgets =Budget.objects.filter(owner=request.user)
    context = {"budgets": budgets}
    return render(request, 'main/budget.html', context)

def add_budget(request):
    budgets =Budget.objects.filter(owner=request.user)
    form = BudgetForm()
    context = {'form': form}
    

    
    if request.method == 'GET':
        return render(request, 'main/add_budget.html', context)
    
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        
        if form.is_valid():
            for budget in budgets:
               if request.POST['category'] == budget.category:
                   messages.success(request,"Budget name already exists")
                   return render(request, 'main/add_budget.html', context)
                    
            data = form.save(commit=False)
            data.owner = request.user
            data.save()
            
            return redirect("budget")
        
  
def edit_budget(request,pk):
    budget = Budget.objects.get(id=pk)
    form = BudgetForm(instance=budget)
    context ={"form": form}
    
    if request.method == 'GET':
        return render(request, 'main/edit_budget.html', context)
    
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        
        if form.is_valid():           
            data = form.save(commit=False)
            data.owner = request.user
            data.save()    
    return redirect("budget")
      