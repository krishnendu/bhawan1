from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account , ProfilePicture , user ,Friend


class AccountAdmin(UserAdmin):
    list_display = ('id' , 'email' , 'username' , 'first_name' , 'last_name' , 'country' , 'phone_number' , 'date_joined' , 'last_login' , 'is_admin' , 'is_staff', 'is_active' , 'is_superuser' , )
    search_fields = ('email' , 'username' , 'first_name' , )
    readonly_fields = ('date_joined' , 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)


admin.site.register(ProfilePicture)

admin.site.register(user)
admin.site.register(Friend)