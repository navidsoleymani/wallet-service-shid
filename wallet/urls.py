from django.conf.urls import url

from wallet import views

urlpatterns = [
    url(
        regex=r'^new/wallet$',
        view=views.WalletCreateAPIView,
        name='create-new-wallet'
    ),
    url(
        regex=r'^list/wallet$',
        view=views.WalletListAPIView,
        name='wallet-list'
    ),
    url(
        regex=r'^list/wallet/pocket_name$',
        view=views.WalletPocketNameListAPIView,
        name='wallet-pocket-name-list'
    ),
    url(
        regex=r'^new/your-pocket$',
        view=views.YourPocketCreateAPIView,
        name='create-new-your-pocket'
    ),
    url(
        regex=r'^list/your-pocket$',
        view=views.YourPocketListAPIView,
        name='your-pocket-list'
    ),
    url(
        regex=r'^list/your-pocket/pocket-name$',
        view=views.YourPocketPocketNameListAPIView,
        name='your-pocket-pocket-name-list'
    ),
    url(
        regex=r'^new/transaction$',
        view=views.TransactionCreateAPIView,
        name='create-new-transaction'
    ),
    url(
        regex=r'^list/transaction$',
        view=views.TransactionListAPIView,
        name='transaction-list'
    ),
    url(
        regex=r'^list/transaction/applied$',
        view=views.TransactionAppliedListAPIView,
        name='applied-transaction-list'
    ),
    url(
        regex=r'^list/transaction/not-applied$',
        view=views.TransactionNotAppliedListAPIView,
        name='not-applied-transaction-list'
    ),
    url(
        regex=r'^list/transaction/wallet$',
        view=views.TransactionWalletListAPIView,
        name='wallet-transaction-list'
    ),
    url(
        regex=r'^list/transaction/your-pocket$',
        view=views.TransactionYourPocketListAPIView,
        name='your-pocket-transaction-list'
    ),

    url(
        regex=r'^list/transaction/owner$',
        view=views.TransactionOwnerListAPIView,
        name='owner-transaction-list'
    ),

]
