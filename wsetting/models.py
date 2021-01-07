from django.db import models


class MaxMiN(models.Model):
    MAXIMUM = 1000000
    maximum = models.FloatField(default=MAXIMUM)
    MINIMUM = 1000
    minimum = models.FloatField(default=MINIMUM)