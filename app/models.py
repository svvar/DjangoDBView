import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    price = models.FloatField(default=0.0, null=False, blank=False)
    date_added = models.DateField(null=False, blank=False, default=datetime.date.today())

    def __str__(self):
        return self.name