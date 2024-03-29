from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard_view, name='dashboard'),
    path("expenses/", views.all_expenses, name='all-expenses'),
    path("expenses/add/", views.add_expenses, name='add-expense'),
    path("expenses/edit/<int:pk>", views.edit_expenses, name='edit-expense'),
    path("expenses/delete/<int:pk>", views.delete_expenses, name='delete-expense'),
    path("expenses_summary", views.expense_category_summary, name='expense-summary'),

    
]
