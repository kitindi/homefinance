from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard_view, name='dashboard'),
    path("expenses/", views.all_expenses, name='all-expenses'),
    path("expenses/add/", views.add_expenses, name='add-expenses'),
    path("expenses/edit/<int:pk>", views.edit_expenses, name='edit-expenses'),
    path("expenses/delete/<int:pk>", views.delete_expenses, name='delete-expenses'),
]
