from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser, Order


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'contact',
        'experience',
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.unregister(Group)
