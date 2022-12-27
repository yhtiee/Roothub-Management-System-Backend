from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Trainees_alumni)
class AdminTraineesAlumni(admin.ModelAdmin):
    pass