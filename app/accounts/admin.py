from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib import admin
from django_otp.admin import OTPAdminSite


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    readonly_fields = ("date_joined", "unique_id")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "phone", "role", 'coins')},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "date_joined", "first_name", "last_name", "is_staff")
    search_fields = ("email", "date_joined", "first_name", "last_name")
    ordering = ("email",)


class OTPAdmin(OTPAdminSite):
    pass


from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

admin_site = OTPAdmin(name="OTPAdmin")

admin_site.register(User)
admin_site.register(TOTPDevice)
