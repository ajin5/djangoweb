from django.contrib import admin
from .models import contactform
from .import models
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.


admin.site.register(contactform)