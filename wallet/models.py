from django.db import models
from uuid import uuid4


class Transaction(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    date = models.DateTimeField(
        null=False,
        blank=False,
        editable=False
    )
    amount = models.FloatField(
        null=False,
        blank=False,
        editable=False
    )
    transaction_information = models.JSONField(
        editable=False
    )
    wallet = models.ForeignKey(
        to='Wallet',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        editable=False
    )
    your_pocket = models.ForeignKey(
        to='YourPocket',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        editable=False
    )
    WALLET_TYPE_CHOICES = [
        ('w', 'Wallet'),
        ('y', 'Your Pocket'),
    ]
    wallet_type = models.CharField(
        max_length=1,
        choices=WALLET_TYPE_CHOICES,
        default='w',
        null=False,
        blank=False,
        editable=False
    )


class Wallet(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    user_id = models.CharField(
        max_length=512,
        null=False,
        blank=False,
        editable=False
    )
    is_block = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        editable=True
    )
    pocket_name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        editable=False
    )
    balance = models.FloatField(
        default=0,
        null=False,
        blank=False,
        editable=True
    )

    def __str__(self):
        return 'Wallet with id "{}", user id "{}" and pocket name "{}".' \
            .format(self.pk, self.user_id, self.pocket_name)

    class Meta:
        unique_together = (
            'pocket_name',
            'user_id'
        )


class YourPocket(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    user_id = models.CharField(
        max_length=512,
        null=False,
        blank=False,
        editable=False
    )
    active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        editable=True
    )
    balance = models.FloatField(
        default=0,
        null=False,
        blank=False,
        editable=True
    )
    expiry_date = models.DateTimeField(
        null=False,
        blank=False,
        editable=False
    )
    your_pocket_information = models.JSONField(
        editable=False
    )

    def __str__(self):
        return 'Wallet with id "{}" , user id {} and expiry date "{}".'. \
            format(self.pk, self.user_id, self.expiry_date)
