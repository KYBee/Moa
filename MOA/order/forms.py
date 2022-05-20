from tkinter import Widget
from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('store', 'receive_place', 'target_people', 'target_money', 'target_time', 'chat_room')
        widgets = {
            'target_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }