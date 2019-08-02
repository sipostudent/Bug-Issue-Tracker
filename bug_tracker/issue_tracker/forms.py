from django import forms

class CreateTicketForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Title',
        max_length=200
    )
    category = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[('bug', 'Bug'), ('feature', 'Feature Request')],
        label='Category'
    )
    details = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

class EditTicketForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Title',
        max_length=200
    )
    category = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[('bug', 'Bug'), ('feature', 'Feature Request')],
        label='Category'
    )
    details = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
