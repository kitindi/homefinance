from django.forms import ModelForm
from .models import Profile
from django.forms.widgets import TextInput,NumberInput,FileInput, Textarea


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['phone_number','full_name','image','bio','location']
        
        widgets = {
            'location':TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600','placeholder':'Dar es Salaam, Tanzania'}),
            'phone_number':TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600'}),
            'full_name':TextInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600','placeholder':'John Smith'}),
            'bio':Textarea(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600','rows':3,'cols':4,'placeholder':'What are you doing for a living ?'}),
            'image':FileInput(attrs={'class': 'py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600'}),
                       
                       
            }