# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/users')
	else:
		form = UserCreationForm()

		args = {'form': form}
		return render (request, 'users/reg_form.html', args)	