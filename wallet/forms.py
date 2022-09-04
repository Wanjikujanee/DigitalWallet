from dataclasses import Field, field, fields
from django import forms
from .models import Account, Card, Customer, Loan, Notifications, ThirdParty, Transaction, Wallet,Receipts,Reward


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"    
class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"   
class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Card
        fields="__all__"    
class ThirdPartyRegistrationForm(forms.ModelForm):
    class Meta:
        model=ThirdParty
        fields="__all__"     
class NotificationsRegistrationForm(forms.ModelForm):  
    class Meta:
        model=Notifications
        fields="__all__"     
class ReceiptsRegistrationForm(forms.ModelForm):
    class Meta:
        model=Receipts
        fields="__all__"
class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields="__all__"    
class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Reward
        fields="__all__"    
class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"               
        
                 
          

       
        
        