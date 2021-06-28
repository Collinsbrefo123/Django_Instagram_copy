from django.forms import ModelForm
from .models import InstaUsers, Feeds


class UsersignupForm(ModelForm):
    class Meta:
        model = InstaUsers
        fields = ['username', 'username', 'lastname', 'email', 'password']


class CreateFeed(ModelForm):
    class Meta:
        model = Feeds
        fields = ['feedTitle', 'imgFeed', 'caption']