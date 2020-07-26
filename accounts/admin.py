from django.contrib import admin

# Register your models here.
from .models import Customer,Order,Products,Tag;

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Products)
admin.site.register(Tag)