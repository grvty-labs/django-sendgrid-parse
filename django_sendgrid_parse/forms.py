from django import forms

from .models import Email


class EmailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['to'] = forms.CharField()
        self.fields['from'] = forms.CharField()
        self.fields['attachments'] = forms.IntegerField()
        self.fields['to_mailbox'].required = False
        self.fields['from_mailbox'].required = False

    def clean(self, *args, **kwargs):
        super(EmailForm, self).clean()
        self.cleaned_data['to_mailbox'] = self.cleaned_data.get('to')
        self.cleaned_data['from_mailbox'] = self.cleaned_data.get('from')

    class Meta:
        model = Email
        exclude = ('attachments', )
        widget = {
            'to_mailbox': forms.HiddenInput(),
            'from_mailbox': forms.HiddenInput(),
        }
