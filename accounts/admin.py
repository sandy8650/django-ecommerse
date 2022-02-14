from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
<<<<<<< HEAD
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm, UserAdminCreationForm
=======
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib.auth import get_user_model
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4

User = get_user_model()


class UserProAdmin(UserAdmin):
<<<<<<< HEAD

    # the forms are used for add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'first_name', 'last_name', 'joined_date', 'last_login', 'is_active')
    filter_horizontal = ()
    list_filter = ('email', 'first_name')
    ordering = ('-joined_date',)
=======
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
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
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
<<<<<<< HEAD
admin.site.unregister(Group)
=======
>>>>>>> 4710397c97df0ed639ec731e8792e78cf5f126f4
