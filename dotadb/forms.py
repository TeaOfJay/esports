from django import forms

class ReplayForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(
            label='Select a file',
            help_text='Dota 2 Replay'
        )