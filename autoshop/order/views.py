# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from autoshop.order.forms import OrderForm


@login_required
def make_order(request):
    order_form = OrderForm(request.POST or None)
    user = request.user
    if request.method == 'POST':
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = user
            order.save()
