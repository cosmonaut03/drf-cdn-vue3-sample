from django.contrib import admin

from apiv1.models.user import User



class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "password",
        "username",
        "id",
        "email",
        "last_login",
        "created_at",
        "role",
        "user_permissions",
        "updated_at",
    )
    ordering = ("-created_at",)
    readonly_fields = ("id", "created_at")


admin.site.register(User)
