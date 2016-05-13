# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class List(models.Model):
    creator = models.ForeignKey('auth.User', related_name='lists')
    name = models.CharField(_('Lista'), max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)


class Product(models.Model):
    list = models.ForeignKey(List, related_name='products')
    name = models.CharField(_('Produto'), max_length=140)
    quantity = models.PositiveSmallIntegerField(_('Quantidade'))
    price = models.DecimalField(_('Preço'), max_digits=19, decimal_places=2)

    def __str__(self):
        return self.name
