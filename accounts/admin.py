from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class UserProAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'joined_date', 'last_login', 'is_active')
    filter_horizontal = ()
    list_filter = ('email', 'first_name', 'username')
    ordering = ('-joined_date',)
    fieldsets = ()
    readonly_fields = ('joined_date', 'last_login')


admin.site.register(UserProfile, UserProAdmin)
