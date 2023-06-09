from django.contrib import admin

from .models import TastModel

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_text','completed','created_at','modified_at')


admin.site.register(TastModel, TaskAdmin)