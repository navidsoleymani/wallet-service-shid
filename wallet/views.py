from rest_framework import generics

from . import serializers
from . import models


class AllTransactionListAPIView(generics.ListAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.AllTransactionListSerializer


class AllTransactionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.AllTransactionDetailSerializer
    lookup_field = 'id'


class WalletCreateAPIView(generics.CreateAPIView):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletCreateSerializer


class WalletListAPIView(generics.ListAPIView):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletListSerializer


class WalletRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletDetailSerializer
    lookup_field = 'id'


class WalletRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.BlockOrActiveWalletSerializer
    lookup_field = 'id'


class WalletTransactionCreateAPIView(generics.CreateAPIView):
    queryset = models.Transaction.objects.filter(wallet_type__exact='w').all()
    serializer_class = serializers.WalletTransactionCreateSerializer


class WalletTransactionListAPIView(generics.ListAPIView):
    queryset = models.Transaction.objects.filter(wallet_type__exact='w').all()
    serializer_class = serializers.WalletTransactionListSerializer


class WalletTransactionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Transaction.objects.filter(wallet_type__exact='w').all()
    serializer_class = serializers.WalletTransactionDetailSerializer
    lookup_field = 'id'


class YourPocketCreateAPIView(generics.CreateAPIView):
    queryset = models.YourPocket.objects.all()
    serializer_class = serializers.YourPocketCreateSerializer


class YourPocketListAPIView(generics.ListAPIView):
    queryset = models.YourPocket.objects.filter(active__exact=True).all()
    serializer_class = serializers.YourPocketListSerializer


class YourPocketRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.YourPocket.objects.filter(active__exact=True).all()
    serializer_class = serializers.YourPocketDetailSerializer
    lookup_field = 'id'


class YourPocketTransactionCreateAPIView(generics.CreateAPIView):
    queryset = models.Transaction.objects.filter(wallet_type__exact='y').all()
    serializer_class = serializers.YourPocketTransactionCreateSerializer


class YourPocketTransactionListAPIView(generics.ListAPIView):
    queryset = models.Transaction.objects.filter(wallet_type__exact='y').all()
    serializer_class = serializers.YourPocketTransactionListSerializer


class YourPocketTransactionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Transaction.objects.filter(wallet_type__exact='y').all()
    serializer_class = serializers.YourPocketTransactionDetailSerializer
    lookup_field = 'id'
