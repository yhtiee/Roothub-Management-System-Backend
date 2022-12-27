from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Trainer)
class AdminTrainersAlumni(admin.ModelAdmin):
    pass