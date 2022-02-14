from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


class UserProAdmin(UserAdmin):

    # the forms are used for add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'first_name', 'last_name', 'joined_date', 'last_login', 'is_active')
    filter_horizontal = ()
    list_filter = ('email', 'first_name')
    ordering = ('-joined_date',)
    readonly_fields = ('joined_date', 'last_login')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Persional Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'admin', 'superadmin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2')
        }),
    )


admin.site.register(User, UserProAdmin)
admin.site.unregister(Group)