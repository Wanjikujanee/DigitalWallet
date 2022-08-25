from django.contrib import admin
from .models import Customer,Wallet,Account,Transaction,Card,ThirdParty,Notifications,Receipts,Loan,Reward


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    search_fields=("first_name","last_name")
class WalletAdmin(admin.ModelAdmin):
     list_display=("active","pin","type",)
     search_fields=("active","pin")
class AccountAdmin(admin.ModelAdmin):
     list_display=("account_type","account_name","destination",)
     search_fields=("account_type","account_name")
class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_type","destination_account","status",)
    search_fields=("transaction_type","destination_account")
class CardAdmin(admin.ModelAdmin):
     list_display=("card_status","signature","issuer",)
     search_fields=("card_status","signature")
class ThirdPartyAdmin(admin.ModelAdmin):
     list_display=("transaction_cost","email","account")
     search_fields=("transaction_cost","email")
class NotificationsAdmin(admin.ModelAdmin):
     list_display=("date_created","message","image")
     search_fields=("date_created","message")
class ReceiptsAdmin(admin.ModelAdmin):
    list_display=("receipt_date","transaction")
    search_fields=("receipt_date","transaction")
class LoanAdmin(admin.ModelAdmin):
     list_display=("loan_term","loan_type","interest_rate",)
     search_fields=("loan_term","loan_type")
class RewardAdmin(admin.ModelAdmin):
     list_display=("date","gender","points",)
     search_fields=("date","gender")
    
    
    
     
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(ThirdParty,ThirdPartyAdmin)
admin.site.register(Notifications,NotificationsAdmin)
admin.site.register(Receipts,ReceiptsAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Reward,RewardAdmin)
