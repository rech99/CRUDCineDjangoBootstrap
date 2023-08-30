from django.contrib import admin
from .models import Genero

class GenerAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Genero, GenerAdmin)