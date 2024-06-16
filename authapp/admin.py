from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import NewUser
from .forms import NewUserCreationForm, NewUserChangeForm
from django.contrib.auth.models import Group

class NewUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = NewUserChangeForm
    add_form = NewUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username','email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(NewUser, NewUserAdmin)
# ... and, if necessary, unregister the Group model from admin.
admin.site.unregister(Group)
