from django import forms
from captcha.fields import CaptchaField

class CommentForm(forms.Form):
    author = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()