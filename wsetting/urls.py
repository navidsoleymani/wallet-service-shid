from django.conf.urls import url

from wsetting import views

urlpatterns = [
    url('transaction/set/minmax/', views.setMinimax, name='set-min-max'),
    url('wallet/block/', views.block, name='wallet-block'),
    url('wallet/unblock/', views.unblock, name='wallet-unblock'),
]