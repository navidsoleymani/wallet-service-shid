from django.conf.urls import url
from wsetting import views

urlpatterns = [
    url(
        regex=r'^transaction-limit$',
        view=views.transaction_limit,
        name='transaction-limit'
    ),
    url(
        regex=r'^expiry-date$',
        view=views.expiry_date,
        name='expiry-date'
    ),

]
