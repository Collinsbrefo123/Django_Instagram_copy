from django.contrib import admin
from .models import InstaUsers, Feeds
# Register your models here.
admin.site.register([InstaUsers, Feeds])
