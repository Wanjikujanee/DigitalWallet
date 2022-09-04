
from django.urls import path
from.views import register_customer, register_notifications, register_receipts, register_reward, register_thirdparty, register_transaction,register_wallet,register_account,register_card,register_loan
urlpatterns = [path("register/",register_customer,name="registration")]
urlpatterns=[path("register/",register_wallet,name="wallet")]
urlpatterns=[path("register/",register_account,name="account")]
urlpatterns=[path("register/",register_card,name="card")]
urlpatterns=[path("register/",register_thirdparty,name="thirdparty")]
urlpatterns=[path("register/",register_notifications,name="notifications")]
urlpatterns=[path("register/",register_receipts,name="receipts")]
urlpatterns=[path("register/",register_loan,name="loan")]
urlpatterns=[path("register/",register_reward,name="reward")]
urlpatterns=[path("register/",register_transaction,name="transaction")]





