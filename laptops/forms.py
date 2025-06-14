from django import forms


class CallMatchForm(forms.Form):
    text_input = forms.CharField(
        label='Just enter some text',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Type something here...'
        })
    )
