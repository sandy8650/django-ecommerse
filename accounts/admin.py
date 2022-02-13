from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'first_name', 'last_name', 'joined_date', 'last_login', 'active')
    filter_horizontal = ()
    list_filter = ('admin', 'staff')
    ordering = ('-joined_date',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Profile', {'fields': ('first_name', 'last_name')}),
        ('Permission', {'fields': ('active', 'staff', 'admin')}),
        (None, {'fields': ('joined_date', 'last_login')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2'),
        }),
    )
    readonly_fields = ('joined_date', 'last_login')


admin.site.register(User, UserProAdmin)
