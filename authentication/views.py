from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.views import View
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# Create your views here.


class  LoginView(View):
    
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:
            user = authenticate(request,username=username,password=password)
            
            if user:
                 login(request, user)
                 return redirect('dashboard')
        messages.error(request,f'Invalid username or password')   
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
            return JsonResponse({'email_error':'Email is already in use'}, status = 409)
        
        return JsonResponse({'email_valid':True})
            
    
class  RegisterView(View):
    
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        # get user data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm-password']
        
        context = { 'field_values': request.POST} 
        # validate
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 8 :
                    messages.warning(request,"Password must be at least 8 characters")
                    return render(request, 'authentication/register.html', context)
                if password != confirmPassword:
                    messages.warning(request,"Password mismatch")
                    return render(request, 'authentication/register.html', context)
                
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                # user.is_active = False
                # email_subject = "Activate your account"
                # email_body = "Test email"
                # email = EmailMessage(
                #         email_subject,
                #         email_body,
                #         "noreply@gmail.com",
                #         [email]
                #         )
                # email.send(fail_silently=False)
                user.save()
                
                return redirect("login")
                  
        # create user account
        return render(request, 'authentication/register.html')
    

# logout user

class Logoutview(View):
    def get(self, request):
        logout(request)
        
        return redirect("login")