from django.forms import ModelForm
from .models import InstaUsers


class UsersignupForm(ModelForm):
    class Meta:
        model = InstaUsers
        fields = ['username', 'username', 'lastname', 'dateofbirth', 'email', 'password']
