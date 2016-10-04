from django.contrib import admin

# Register your models here.
from .models import Join


class JoinAdmin(admin.ModelAdmin):
    list_display = ['email','refered_by','timestamp','updated']
    class Meta:
        model = Join


admin.site.register(Join, JoinAdmin)
