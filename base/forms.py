from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Rooms


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'
        exclude = ['host','participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']