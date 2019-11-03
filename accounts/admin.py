from django.contrib import admin
from .models import MyUser, UserCode

admin.site.register(MyUser)
admin.site.register(UserCode)
