from django.contrib import admin

from core.models import CustomUser


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'username')
    list_filter = ('is_staff', 'is_active', 'is_superuser')


admin.site.register(CustomUser, UserAdmin)
# Register your models here.
