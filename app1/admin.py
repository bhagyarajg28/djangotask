from django.contrib import admin

from .models import Branches
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(Branches)
class BranchesAdmin(ImportExportModelAdmin):
    pass
