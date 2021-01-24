from itertools import chain
from django.db import models
from uuid import uuid4
import MESSAGE


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
    pocket_name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        editable=False
    )
    block = models.BooleanField(
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
    info = models.JSONField(
        editable=False,
        null=True,
        blank=True,
    )

    def transaction_is_valid(self, value: float) -> [bool, str]:
        res = value + self.balance
        if res > 0:
            self.block = False
            self.balance = res
            self.save()
            return True, ''
        else:
            if self.block:
                self.block = True
                self.save()
                return False, MESSAGE.WALLET_IS_BLOCK
            else:
                self.block = True
                self.balance = res
                self.save()
                return True, ''

    def set_default(self):
        self.block = False
        self.balance = 0

    @property
    def is_block(self):
        if self.block or self.balance <= 0:
            self.block = True
            return True
        self.block = False
        return False

    @property
    def to_be_blocked(self):
        self.block = True

    @property
    def to_be_activated(self):
        self.block = False

    def __str__(self):
        return 'Wallet with id "{}", user id "{}" and pocket name "{}".' \
            .format(self.pk, self.user_id, self.pocket_name)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data

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
    pocket_name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        editable=False
    )
    active = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        editable=True,
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

    info = models.JSONField(
        editable=False,
        null=True,
        blank=True,
    )

    def transaction_is_valid(self, value: float) -> [bool, str]:
        res = value + self.balance
        import datetime
        now = datetime.datetime.now(datetime.timezone.utc)
        if res < 0:
            err_msg = MESSAGE.YOUR_POCKET_NOT_ENOUGH
            return False, err_msg
        if self.active is False:
            err_msg = MESSAGE.YOUR_POCKET_IS_NOT_ACTIVE
            return False, err_msg
        if self.expiry_date < now:
            err_msg = MESSAGE.YOUR_POCKET_EXPIRED
            return False, err_msg
        else:
            self.balance = res
            self.save()
            return True, ''

    def set_default(self):
        from wsetting.models import ExpiryDate
        import datetime
        s = ExpiryDate.objects.filter(pocket_name__exact=self.pocket_name).last()
        if s is None:
            s = ExpiryDate.objects.filter(pocket_name__exact='__all__').last()
        self.expiry_date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=s.day)
        self.active = True

    @property
    def is_active(self):
        import datetime
        now = datetime.datetime.now(datetime.timezone.utc)
        if self.active is False or self.expiry_date < now:
            self.active = False
            return False
        return True

    def __str__(self):
        return 'Wallet with id "{}" , user id {} and expiry date "{}".'. \
            format(self.pk, self.user_id, self.expiry_date)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data


class Transaction(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    date = models.DateTimeField(
        null=False,
        blank=False,
        editable=False
    )
    # user_id
    owner = models.CharField(
        max_length=512,
        null=False,
        blank=False,
        editable=False
    )
    amount = models.FloatField(
        null=False,
        blank=False,
        editable=False
    )
    info = models.JSONField(
        editable=False,
        null=True,
        blank=True,
    )
    WALLET_TYPE_CHOICES = [
        ('wallet', 'wallet'),
        ('your_pocket', 'your_pocket'),
    ]
    type = models.CharField(
        max_length=20,
        choices=WALLET_TYPE_CHOICES,
        null=False,
        blank=False,
        editable=False
    )
    wallet = models.ForeignKey(
        to=Wallet,
        blank=True,
        null=True,
        editable=False,
        on_delete=models.CASCADE,
    )
    your_pocket = models.ForeignKey(
        to=YourPocket,
        blank=True,
        null=True,
        editable=False,
        on_delete=models.CASCADE,
    )
    applied = models.BooleanField(
        editable=False,
        blank=True,
        null=True,
    )

    def set_default(self):
        import datetime
        self.date = datetime.datetime.now(datetime.timezone.utc)

    @property
    def is_valid(self) -> bool:
        from wsetting.models import TransactionLimit
        s = TransactionLimit.objects.last()
        if abs(self.amount) < s.low:
            self.applied = False
            self.save()
            raise Exception(MESSAGE.TRANSACTION_LOWER)

        if abs(self.amount) > s.high:
            self.applied = False
            self.save()
            raise Exception(MESSAGE.TRANSACTION_UPER)

        if self.type == 'wallet':
            is_valid, err_msg = self.wallet.transaction_is_valid(self.amount)
            if is_valid:
                self.applied = True
                self.save()
                return True
            else:
                self.applied = False
                self.save()
                raise Exception(err_msg)
        if self.type == 'your_pocket':
            is_valid, err_msg = self.your_pocket.transaction_is_valid(self.amount)
            if is_valid:
                self.applied = True
                self.save()
                return True
            else:
                self.applied = False
                self.save()
                raise Exception(err_msg)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data
