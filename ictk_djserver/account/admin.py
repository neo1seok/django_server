from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'date_of_birth', 'is_admin','user_name','position','depart')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields':
                               ('date_of_birth','user_name','phone_number','mobile_number','position','depart','address',)
                           }
        ),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2',)}

         ),
        ('Personal info', {'fields':
                               ( 'user_name', 'phone_number', 'mobile_number', 'position', 'depart',
                                'address',)
                           }
         ),

    )
    search_fields = ('email','user_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)