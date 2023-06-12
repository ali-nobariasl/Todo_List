from django.contrib import admin

from .models import TastModel , Profile




class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_text','completed','created_at','modified_at')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','created_at','modified_at')


admin.site.register(TastModel, TaskAdmin)
admin.site.register(Profile, ProfileAdmin)