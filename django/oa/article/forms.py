from  django import forms

class AddForm(forms.Form):
    a = forms.IntegerField(required=True, label='姓名')
    b = forms.IntegerField(required=False)