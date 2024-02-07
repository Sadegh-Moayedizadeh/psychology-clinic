from django import forms

class ContentForm(forms.Form):
    name = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
