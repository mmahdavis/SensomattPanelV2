"""Docstring."""
from django.contrib import admin
from .models import Nurse, Patient, Bed, Bed_History, Notifications, Token

admin.site.register(Nurse)
admin.site.register(Bed)
admin.site.register(Bed_History)
admin.site.register(Patient)
admin.site.register(Notifications)
admin.site.register(Token)
