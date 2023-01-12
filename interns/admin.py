from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Interns)
class AdminIntern(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "other_names",
        "email",
        "course_learning",
        "course_duration",
        "training_fee",
        "amount_paid",
        "balance", 
        "phone_number",
        "location",
        "registrationDate",
        "profile_picture",
    ]