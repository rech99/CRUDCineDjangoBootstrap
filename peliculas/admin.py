from django.contrib import admin
from .models import Pelicula

# Register your models here.

class PelisAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Pelicula, PelisAdmin)