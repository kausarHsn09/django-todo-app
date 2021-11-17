from django.db import models
from django import forms
from django.db.models import fields
from django.forms import ModelForm

# Create your models here.

class input_model(models.Model):
    textInput=models.CharField(max_length=500)
   
    def __str__(self):
        return self.textInput



class getTodo(ModelForm):
    class Meta:
        model=input_model
        fields='__all__'
        widgets={
            'textInput':forms.TextInput(attrs={'class':'textField','placeholder': 'Add todo'})
        }
       