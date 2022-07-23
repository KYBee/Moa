from tkinter import Widget
from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('store', 'target_time', 'target_people', 'target_money', 'receive_place', 'chat_room')
        widgets = {
            'target_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }