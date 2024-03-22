from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
# Create your views here.


class  LoginView(View):
    
    def get(self, request):
        return render(request, 'authentication/login.html')
    

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
            
    
class  RegisterView(View):
    
    def get(self, request):
        return render(request, 'authentication/register.html')
    

