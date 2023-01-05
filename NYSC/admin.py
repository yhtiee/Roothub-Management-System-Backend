from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(NYSC)
class AdminNYSC(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "other_names",
        "email",
        "phone_number",
        "location",
        "registrationDate",
        "profile_picture",
        "attached_area"
    ]
