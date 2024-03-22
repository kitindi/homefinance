from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from validate_email import validate_email
# Create your views here.


class  LoginView(View):
    
    def get(self, request):
        return render(request, 'authentication/login.html')
    
# validate username if exists
class  UsernameValidationView(View):
    
    def post(self, request):
        # accessing data from user in json format
        data = json.loads(request.body)
        username = data['username']
        
        # check if username contains alphanumeric characters only
        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username should only contain alphanumeric characters'}, status = 400)
        
        # check if username already exists in the database
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Username is already in use'}, status = 409)
        
        return JsonResponse({'username_valid':True})

# validate email in right format ans if exists
class  EmailValidationView(View):
    
    def post(self, request):
        # accessing data from user in json format
        data = json.loads(request.body)
        email = data['email']
        
        # check if username contains alphanumeric characters only
        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'}, status = 400)
        
        # check for valid email and if already exists in the database
        if User.objects.filter(email=email).exists():
            return JsonResponse({'username_error':'Email is already in use'}, status = 409)
        
        return JsonResponse({'email_valid':True})
            
    
class  RegisterView(View):
    
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        # get user data
        uername = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm-password']
        # validate
        # create user account
        return render(request, 'authentication/register.html')
    

