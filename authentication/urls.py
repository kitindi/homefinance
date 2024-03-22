from django.urls import path
# decorator for backwards compatibility
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path("", views.LoginView.as_view(), name='login'),
    path("register/", views.RegisterView.as_view(), name='register'),
    path('valiadte_username/',csrf_exempt(views.UsernameValidationView.as_view()), name='valiad_username')
]
