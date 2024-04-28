from django.contrib import admin
from .models import User,Products,Login

admin.site.register(Products)
admin.site.register(User)
admin.site.register(Login)
