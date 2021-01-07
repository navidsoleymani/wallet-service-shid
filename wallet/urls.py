from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^wallet/transaction/new/$',
        view=views.WalletTransactionCreateAPIView.as_view(),
        name='new-wallet-transaction'
    ),
    url(
        regex=r'^wallet/transaction/list/$',
        view=views.WalletTransactionListAPIView.as_view(),
        name='wallet-transaction-list'
    ),
    # url(
    #     regex=r'^wallet/transaction/(?P<id>\d+)/detail/$',
    #     view=views.WalletTransactionRetrieveAPIView.as_view(),
    #     name='wallet-transaction-detail'
    # ),
    url(
        regex=r'^wallet/new/$',
        view=views.WalletCreateAPIView.as_view(),
        name='create-new-wallet'
    ),
    url(
        regex=r'^wallet/list/$',
        view=views.WalletListAPIView.as_view(),
        name='wallet-list'
    ),
    # url(
    #     regex=r'^wallet/(?P<id>\d+)/detail/$',
    #     view=views.WalletRetrieveAPIView.as_view(),
    #     name='wallet-detail'
    # ),
    url(
        regex=r'^wallet/(?P<id>\d+)/update/$',
        view=views.WalletRetrieveUpdateAPIView.as_view(),
        name='update-wallet'
    ),
    url(
        regex=r'^your-pocket/transaction/new/$',
        view=views.YourPocketTransactionCreateAPIView.as_view(),
        name='new-your-pocket-transaction'
    ),
    url(
        regex=r'^your-pocket/transaction/list/$',
        view=views.YourPocketTransactionListAPIView.as_view(),
        name='your-pocket-transaction-list'
    ),
    # url(
    #     regex=r'^your-pocket/transaction/(?P<id>\d+)/detail/$',
    #     view=views.YourPocketTransactionRetrieveAPIView.as_view(),
    #     name='your-pocket-transaction-detail'
    # ),
    url(
        regex=r'^your-pocket/new/$',
        view=views.YourPocketCreateAPIView.as_view(),
        name='create-new-your-pocket'
    ),
    url(
        regex=r'^your-pocket/list/$',
        view=views.YourPocketListAPIView.as_view(),
        name='wallet-list-your-pocket'
    ),
    # url(
    #     regex=r'^your-pocket/(?P<id>\d+)/detail/$',
    #     view=views.YourPocketRetrieveAPIView.as_view(),
    #     name='wallet-detail-your-pocket'
    # ),
    url(
        regex=r'^all/transaction/list/$',
        view=views.AllTransactionListAPIView.as_view(),
        name='all-transaction-list'
    ),
    # url(
    #     regex=r'^all/transaction/(?P<id>\d+)/detail/$',
    #     view=views.AllTransactionRetrieveAPIView.as_view(),
    #     name='all-transaction-detail'
    # ),
]
