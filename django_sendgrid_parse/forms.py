from django import forms

from .models import Email


class EmailForm(forms.ModelForm):
    attachments = forms.IntegerField()

    class Meta:
        model = Email
        exclude = ('attachments', )
