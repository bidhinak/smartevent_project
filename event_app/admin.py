from django.contrib import admin

from event_app import models


admin.site.register(models.Login)
admin.site.register(models.student)
admin.site.register(models.teacher)

