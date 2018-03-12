from django import  forms


class FormDetails(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_id = forms.EmailField()