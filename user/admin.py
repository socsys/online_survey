from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile


class CustomUserAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('id', 'nickname', 'is_staff', 'is_admin')
    fieldsets = (
        (None, {'fields': ('nickname', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nickname', 'password1', 'password2'),
        }),
    )
    search_fields = ('nickname',)
    ordering = ('id',)


admin.site.register(UserProfile, CustomUserAdmin)
