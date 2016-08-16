from django import forms

from .models import Email


class EmailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['to_mailbox'].required = False
        self.fields['from_mailbox'].required = False
        self.fields['to'] = self.fields['to_mailbox']
        self.fields['from'] = self.fields['from_mailbox']
        self.fields['attachments'] = forms.IntegerField()

    def clean(self):
        cleaned_data = super(EmailForm, self).clean()
        cleaned_data['to_mailbox'] = self.cleaned_data.get('to')
        cleaned_data['from_mailbox'] = self.cleaned_data.get('from')
        return cleaned_data

    class Meta:
        model = Email
        exclude = ('attachments', )
        widget = {
            'to_mailbox': forms.HiddenInput,
            'from_mailbox': forms.HiddenInput,
        }
