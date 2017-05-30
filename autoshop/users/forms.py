# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class SignInForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': u'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': u'Пароль'}))


class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'number', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': u'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': u'Фамилия'}),
            'email': forms.EmailInput(attrs={'placeholder': u'Email'}),
            'number': forms.TextInput(attrs={'placeholder': u'Номер телефона'}),
            'password': forms.PasswordInput(attrs={'placeholder': u'Пароль'})
        }

    def save(self):
        user = super(SignUpForm, self).save()
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
