from django.contrib import admin
from .models import Customer,Wallet,Transaction,Card,ThirdParty,Account,Receipts,Loan,Reward,Notifications


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    search_fields=("first_name","last_name",)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Reward)
admin.site.register(Loan)
admin.site.register(Account)
admin.site.register(Receipts)
admin.site.register(Notifications)
