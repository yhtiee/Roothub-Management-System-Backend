from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Trainees_general)
class AdminTrainees(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "other_names",
        "email",
        "phone_number",
        "course_learning",
        "course_duration",
        "training_fee",
        "amount_paid",
        "balance", 
        "location",
        "registrationDate",
        "profile_picture",
    ]
