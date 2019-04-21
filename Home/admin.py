from django.contrib import admin

from .models import Sanpham
# Register your models here.

class SanphamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sanpham, SanphamAdmin)
