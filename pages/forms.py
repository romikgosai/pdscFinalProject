from email import message
from django import forms
from django.forms import fields, widgets
from pages.models import Contact
 
class MyForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ["name", "email","message"]
    widgets = {
      'name':forms.TextInput(attrs={
        'name':"name",
        'type':"text", 
        'class':"form-control col-md-6",
        'id':"name", 
        'placeholder':"Your Name"
      }),
      'email':forms.EmailInput(attrs={
        'name':'email',
        'type':'text',
        'class':'form-control col-md-6',
        'id':'email',
        'placeholder':'Your Email',
      }),
      'message':forms.Textarea(attrs={
        'name':'message',
        'rows':'6',
        'class':'form-control col-md-12',
        'id':'message',
        'placeholder':'Your message',

      })
    }