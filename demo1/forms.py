# -*-coding:utf-8-*-
# Author:Ds
from . import models
from django import forms
from multiselectfield.forms.fields import MultiSelectFormField

class BSForm(forms.ModelForm):

    def __init__(self,request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field, (MultiSelectFormField, forms.BooleanField)):
                continue
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请填写{}'.format(field.__dict__['label'])

        self.fields['user'].choices = [(request.user_obj.pk, request.user_obj)]


class PlayerScoreRankingFrom(BSForm):

    class Meta:
        model=models.PlayerScoreRanking
        fields='__all__'

class RegForm(forms.ModelForm):

    class Meta:
        model = models.Users
        fields = '__all__'  # 全局的字段

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '请输入用户名', 'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'placeholder': '请输入密码', 'autocomplete': 'off'}),
        }

