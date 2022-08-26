from django.contrib import admin
from .models import Customer,Wallet,Account,Transaction,Card,ThirdParty,Notifications,Receipts,Loan,Reward


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","gender","nationality","id_number","marital_status")
    search_fields=("first_name","last_name","email","gender","nationality","id_number","marital_status")
class WalletAdmin(admin.ModelAdmin):
     list_display=("active","pin","type","balance","currency","active")
     search_fields=("active","pin","type","balance","currency","active")
class AccountAdmin(admin.ModelAdmin):
     list_display=("account_type","account_name","destination","savings","wallet","destination")
     search_fields=("account_type","account_name","destination","savings","wallet","destination")
class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_type","destination_account","status","receipt","thirdparty","Account_origin")
    search_fields=("transaction_type","destination_account","status","receipt","thirdparty","Account_origin")
class CardAdmin(admin.ModelAdmin):
     list_display=("card_status","signature","issuer","card_type","card_name","card_number")
     search_fields=("card_status","signature","issuer","card_type","card_name","card_number")
class ThirdPartyAdmin(admin.ModelAdmin):
     list_display=("transaction_cost","email","account","id_number","phone_Number")
     search_fields=("transaction_cost","email","account","id_number","phone_Number")
class NotificationsAdmin(admin.ModelAdmin):
     list_display=("date_created","message","image","recipient","time","status")
     search_fields=("date_created","message","Image","recipient","time","status")
class ReceiptsAdmin(admin.ModelAdmin):
    list_display=("receipt_date","transaction","total_amount","receipt_type","account_number")
    search_fields=("receipt_date","transaction","total_amount","receipt_type","account_number")
class LoanAdmin(admin.ModelAdmin):
     list_display=("loan_term","loan_type","interest_rate","due_date","amount","duration")
     search_fields=("loan_term","loan_type","interest_rate","due_date","amount","duration")
class RewardAdmin(admin.ModelAdmin):
     list_display=("date","gender","points","customer_id","wallet","transaction")
     search_fields=("date","gender","points","customer_id","wallet","transaction")
     
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
