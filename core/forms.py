from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="სახელი")
    email = forms.EmailField(label="ელ.ფოსტა")
    message = forms.CharField(widget=forms.Textarea, label="შეტყობინება")
