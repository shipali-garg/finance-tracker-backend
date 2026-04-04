from django.contrib import admin

# Register your models here.
from .models import Transaction, Profile

admin.site.register(Transaction)
admin.site.register(Profile)