from django.contrib import admin

from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Personal Info', 
            {
                'fields': (
                    'username',
                    'email', 
                    'first_name', 
                    'last_name',
                    'avatar',
                )
            }
        ),
        (
            'Account info',
            {
                'fields': (
                    'balance',
                    'xp',
                    'account_type'
                )
            }
        )
        ,
        (
            'Additional Info', 
            {
                'fields': (
                    'last_login', 
                    'date_joined', 
                )
            }
        ),
        (
            'Staff Info', 
            {
                'fields': (
                    'is_active', 
                    'is_staff', 
                    'is_superuser', 
                    'user_permissions', 
                    'groups'
                ), 
                'classes': ('collapse',)
            }
        ),
    )