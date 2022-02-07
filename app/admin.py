from django.contrib import admin

from app.models import Number


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ('value', 'created_at')
