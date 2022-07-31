"""Admin"""
from django.contrib import admin
from .models import User
# pylint: disable=C0304
# Register your models here.
admin.site.register(User)