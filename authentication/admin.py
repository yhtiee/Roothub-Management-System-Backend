from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass

@admin.register(BranchManagers)
class AdminBranch(admin.ModelAdmin):
    pass
