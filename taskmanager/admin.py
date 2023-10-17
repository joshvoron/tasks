from django.contrib import admin

# Register your models here.
from .models import TaskModel, ColorModel

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','user_color','expiration_date','creation_date')

class ColorAdmin(admin.ModelAdmin):
    list_display = ('name','color')

admin.site.register(TaskModel, TaskAdmin)
admin.site.register(ColorModel, ColorAdmin)