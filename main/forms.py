from django import forms


class ContactForm(forms.Form):
    email = forms.CharField(label='ваш E-Mail', widget=forms.TextInput)

    subject = forms.CharField(label='Тема', widget=forms.TextInput)

    content = forms.CharField(label='Текст', widget=forms.Textarea)
