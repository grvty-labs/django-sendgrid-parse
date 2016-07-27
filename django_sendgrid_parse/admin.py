from django.contrib import admin

from . import models

admin.site.register(models.Attachment)
admin.site.register(models.Email)
