from django import forms

from core.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('fullname', 'email', 'subject', 'message')

        widgets = {
            "fullname": forms.TextInput(attrs={"class": 'form-control', "placeholder": 'نام خود را بنویسید'}),
            "email": forms.TextInput(attrs={"class": 'form-control', "placeholder": 'ایمیل خود را بنویسید'}),
            "subject": forms.TextInput(attrs={"class": 'form-control', "placeholder": 'موضوع خود را بنویسید'}),
            "message": forms.Textarea(attrs={"class": 'form-control', "placeholder": 'متن پیام خود را بنویسید'}),
        }
