from django.shortcuts import redirect, render
import os
import json
from django.conf import settings
from .models import Userpreference
from django.contrib import messages
# Create your views here.


def preferences(request):
    
    exists = Userpreference.objects.filter(user = request.user).exists()
    user_preferences = None
    
    currencyData = []
    file_path = os.path.join(settings.BASE_DIR,'currencies.json')

    with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
    for k, v in data.items():
            currencyData.append({"name":k,"value":v})
         
    
    if exists:
        user_preferences = Userpreference.objects.get(user = request.user) 
    
     
 
    if request.method == 'GET':
       
        return render(request, "main/preferences.html",{"currencies":currencyData})
    
    else:
        currency = request.POST['currency']
        # update if the currency data exists
        if exists:
            user_preferences.currency = currency
            user_preferences.save()
        else:
        # create if currency data does not exist
            Userpreference.objects.create(user=request.user, currency=currency)
        
        messages.success(request, "currency is set successfully")
        
    return render(request, "main/preferences.html",{"currencies":currencyData,'user_preferences':user_preferences.currency})
            
    # import pdb
    # pdb.set_trace()
        
    
   
   