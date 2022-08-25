from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender_choice = (
       ('a', 'Male'),
       ('b', 'Female'),
   )
    gender = models.CharField(max_length=15, choices=gender_choice)
    address=models.CharField(max_length=15)
    age=models.IntegerField()
    nationality=models.CharField(max_length=15)
    id_number=models.CharField(max_length=15,blank=True, null=True)
    phonenumber=models.CharField(max_length=15)
    email=models.EmailField()
    marital_status_choice = (
       ('a', 'Married'),
       ('b', 'Single'),
        ('b', 'Others'),
   )
    marital_status=models.CharField(max_length=15,choices = marital_status_choice)
    signature=models.ImageField(upload_to='signature_pictures/',default=timezone.now)
    date_created = models.DateTimeField(default=timezone.now)
    employment_status=models.BooleanField()
    
class Wallet(models.Model):
    balance=models.IntegerField()
    customer=models.OneToOneField('Customer', on_delete=models.CASCADE,related_name='Wallet_customer')
    pin=models.IntegerField()
    active=models.BooleanField()
    date_created=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=20)
    
class Account(models.Model):
    ACCOUNT_TYPE_CHOICE= (
       ('a', 'Assets'),
       ('b', 'Liabilities'),
       ('c','Equity'),
   )
    account_type=models.CharField(max_length=20,choices=ACCOUNT_TYPE_CHOICE)
    account_name=models.CharField(max_length=20)
    savings=models.IntegerField()
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')
    destination=models.CharField(max_length=15)
    
class Transaction(models.Model):
    transaction_type=models.CharField(max_length=10)
    destination_account=models.ForeignKey('Account', on_delete=models.CASCADE,related_name='Transaction_destination_account',default=None,null=True)
    transaction_date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=15)  
    
class Card(models.Model):
    date_Issued=models.DateTimeField(default=timezone.now)
    card_status= models.CharField(max_length=15)
    security_code=models.IntegerField()
    signature=models.ImageField(upload_to='signature_pictures/')
    issuer=models.CharField(max_length=15)
    account=models.ForeignKey('Account', on_delete=models.CASCADE,related_name='Card_account') 
   
class ThirdParty(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    phone_Number=models.IntegerField()
    transaction_cost=models.IntegerField()
    account=models.ForeignKey('Account', on_delete=models.CASCADE,related_name='ThirdPary_account')
    active=models.BooleanField()
    
class Notifications(models.Model):
    date_created=models.DateTimeField(default=timezone.now)
    message=models.CharField(max_length=15)
    isactive=models.BooleanField()
    image=models.ImageField(upload_to='profile_pictures/')
 
class Receipts(models.Model):
    receipt_date=models.DateTimeField(default=timezone.now)
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE,related_name='Reciepts_transaction')
    recipt_File=models.FileField(upload_to='wallet/')
 
class Loan(models.Model):        
    loan_type=models.CharField(max_length=25)
    amount=models.IntegerField()
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE,related_name='Loan_wallet')
    date=models.DateTimeField(default=timezone.now)
    loan_term=models.IntegerField()
    due_date=models.DateField(default=timezone.now)
    loan_balance=models.IntegerField()
    duration=models.CharField(max_length=15)
    interest_rate=models.IntegerField()
    status=models.CharField(max_length=15)
 
class Reward(models.Model):
    wallet=models.ForeignKey('wallet',on_delete=models.CASCADE,related_name='Reward_wallet')
    points=models.CharField(max_length=25)
    date=models.DateTimeField(default=timezone.now)
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE,related_name='Reward_transaction')
    GENDER_CHOICES = (
       ('a', 'Male'),
       ('b', 'Female'),
   )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)

    


 

    


