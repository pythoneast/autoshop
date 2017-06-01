# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.exceptions import ValidationError

from autoshop.order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_fields(self):
        address = self.cleaned_data['address']
        if len(address) < 2:
            raise ValidationError(u'Введите адрес')
        return address
