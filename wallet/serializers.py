from rest_framework import serializers
from datetime import datetime

from . import models


class AllTransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'


class AllTransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'


class YourPocketCreateSerializer(serializers.Serializer):
    id = serializers.CharField(
        read_only=True
    )
    user_id = serializers.CharField(
        required=True,
        allow_null=False
    )
    balance = serializers.FloatField(
        read_only=True
    )
    active = serializers.BooleanField(
        read_only=True
    )
    expiry_date = serializers.DateTimeField(
        read_only=True
    )
    your_pocket_information = serializers.JSONField(
        allow_null=True
    )

    def create(self, validated_data):
        last_your_pocket = models.YourPocket.objects. \
            filter(user_id__exact=validated_data['user_id']). \
            filter(active__exact=True)
        if len(last_your_pocket) != 0:
            raise Exception('An active account is available for this user.')
        obj = models.YourPocket()
        obj.active = True
        obj.balance = 0
        from datetime import datetime, timedelta
        obj.expiry_date = datetime.now() + timedelta(days=30)
        obj.your_pocket_information = validated_data['your_pocket_information']
        obj.user_id = validated_data['user_id']
        obj.save()
        return obj


class YourPocketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.YourPocket
        fields = '__all__'


class YourPocketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.YourPocket
        fields = '__all__'


class YourPocketTransactionCreateSerializer(serializers.Serializer):
    id = serializers.CharField(
        read_only=True,
        allow_null=False
    )
    date = serializers.DateTimeField(
        read_only=True,
        default=datetime.now()
    )
    amount = serializers.FloatField(
        required=True,
        allow_null=False
    )
    transaction_information = serializers.JSONField(
        required=False,
        allow_null=True
    )
    your_pocket = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=models.YourPocket.objects.all()
    )

    def create(self, validated_data):
        obj = models.Transaction()
        obj.date = datetime.now()
        from wsetting.models import MaxMiN
        minmax = MaxMiN.objects.first()
        if minmax is None:
            minmax = MaxMiN()
        minimum = minmax.minimum
        maximum = minmax.maximum

        amount = validated_data['amount']
        if abs(amount) >= maximum:
            raise Exception("amount not true")
        if abs(amount) <= minimum:
            raise Exception("amount not true")
        obj.amount = amount
        obj.transaction_information = validated_data['transaction_information']
        obj.your_pocket = validated_data['your_pocket']
        obj.wallet_type = 'y'
        obj.save()
        yp = models.YourPocket.objects. \
            filter(pk=validated_data['your_pocket'].id).first()
        yp.balance = yp.balance + validated_data['amount']
        yp.save()
        return obj


class YourPocketTransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'


class YourPocketTransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'


class WalletCreateSerializer(serializers.Serializer):
    id = serializers.CharField(
        read_only=True,
        allow_null=False
    )
    user_id = serializers.CharField(
        required=True,
        allow_null=False
    )
    pocket_name = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
        max_length=128
    )
    balance = serializers.FloatField(
        read_only=True,
        default=0
    )
    is_block = serializers.BooleanField(
        read_only=True,
        default=False
    )

    def create(self, validated_data):
        obj = models.Wallet()
        obj.user_id = validated_data['user_id']
        obj.pocket_name = validated_data['pocket_name']
        obj.save()
        return obj


class WalletListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wallet
        fields = '__all__'


class WalletDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wallet
        fields = '__all__'


class BlockOrActiveWalletSerializer(serializers.Serializer):
    id = serializers.CharField(
        read_only=True
    )
    user_id = serializers.CharField(
        read_only=True
    )
    pocket_name = serializers.CharField(
        read_only=True
    )
    balance = serializers.FloatField(
        read_only=True
    )
    is_block = serializers.BooleanField(
        required=True,
        allow_null=False
    )


class WalletTransactionCreateSerializer(serializers.Serializer):
    id = serializers.CharField(
        read_only=True,
        allow_null=False
    )
    date = serializers.DateTimeField(
        read_only=True,
        default=datetime.now()
    )
    amount = serializers.FloatField(
        required=True,
        allow_null=False
    )
    transaction_information = serializers.JSONField(
        required=False,
        allow_null=False
    )
    wallet = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=models.Wallet.objects.all()
    )

    def create(self, validated_data):
        obj = models.Transaction()
        obj.date = datetime.now()

        from wsetting.models import MaxMiN
        minmax = MaxMiN.objects.first()
        if minmax is None:
            minmax = MaxMiN()
        minimum = minmax.minimum
        maximum = minmax.maximum

        amount = validated_data['amount']
        if abs(amount) >= maximum:
            raise Exception("amount not true")
        if abs(amount) <= minimum:
            raise Exception("amount not true")
        obj.amount = amount
        obj.transaction_information = validated_data['transaction_information']
        obj.wallet = validated_data['wallet']
        obj.wallet_type = 'w'
        obj.save()
        wlt = models.Wallet.objects. \
            filter(pk=validated_data['wallet'].id).first()
        wlt.balance = wlt.balance + validated_data['amount']
        wlt.save()
        return obj


class WalletTransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'


class WalletTransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'
