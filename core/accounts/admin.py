from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

# Register your models here.
class CustomUserAdmin (UserAdmin):
    model = CustomUser
    list_display = ('email', 'password', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('email',)

    fieldsets = (
        ('Authentication', {"fields": ("email", "password")}),
        ('permissions', {"fields": ("is_staff", "is_active")}),
        ('group permissions', {"fields": ("groups", "user_permissions")}),
        ('important date', {"fields": ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions",
            )}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)