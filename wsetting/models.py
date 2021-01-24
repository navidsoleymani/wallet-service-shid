from itertools import chain

from django.db import models
import datetime

HIGH_TRANSACTION_LIMIT = 1000000
LOW_TRANSACTION_LIMIT = 1000
EXPIRY_DATE = 30


class TransactionLimit(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    high = models.FloatField()
    low = models.FloatField()

    def set_default(self):
        self.high = HIGH_TRANSACTION_LIMIT
        self.low = LOW_TRANSACTION_LIMIT

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


class ExpiryDate(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    day = models.IntegerField()
    pocket_name = models.CharField(
        max_length=128,
    )

    def set_default(self):
        self.day = EXPIRY_DATE
        self.pocket_name = '__all__'

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
