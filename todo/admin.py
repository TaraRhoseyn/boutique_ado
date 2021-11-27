from django.contrib import admin

# Importing our Item class from the models dir
# This exposes it to admin user
from .models import Item

# Register your models here.
admin.site.register(Item)
