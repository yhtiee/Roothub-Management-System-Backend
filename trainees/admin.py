from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Trainees_general)
class AdminTrainees(admin.ModelAdmin):
    pass
