from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Expense(models.Model):
    
    EXPENSE_CATEGORY = (('Education', 'Education'),('Groceries', 'Groceries'),('Transportation', 'Transportation'),('Utilities', 'Utilities'),('Fixed expenses', 'Fixed expenses'),('Savings contributions', 'Savings contributions'))
    amount = models.FloatField()
    merchant = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, choices=EXPENSE_CATEGORY)
    date = models.DateField(default =now)
    payment_method = models.CharField(max_length=255, null=True)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.category+ " " +"  payed to  " + " "+ self.merchant + " through "+ " " + self.payment_method 
    
    
    class Meta:
        ordering=["-date"]
    

