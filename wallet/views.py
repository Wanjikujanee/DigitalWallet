from urllib import request
from django.shortcuts import render
from.forms import CustomerRegistrationForm, LoanRegistrationForm,NotificationsRegistrationForm, ReceiptsRegistrationForm,WalletRegistrationForm,AccountRegistrationForm,CardRegistrationForm,ThirdPartyRegistrationForm,RewardRegistrationForm,TransactionRegistrationForm

# Create your views here.
def register_customer(request):
    form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})

def register_wallet(request):
    form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})

def register_account(request):
    form=AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})
def register_card(request):
    form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})
def register_thirdparty(request):
    form=ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{"form":form})
def register_notifications(request):
    form=NotificationsRegistrationForm()
    return render(request,"wallet/register_notifications.html",{"form":form})
def register_receipts(request):
    form=ReceiptsRegistrationForm()
    return render(request,"wallet/register_receipts.html",{"form":form})
def register_loan(request):
    form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form})
def register_reward(request):
    form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form})
def register_transaction(request):
    form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})


    
    
    
