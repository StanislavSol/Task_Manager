from django.contrib import admin
from task_manager.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined')
    search_user = ['username', 'first_name', 'last_name']
    list_filter = (('date_joined', admin.DateFieldListFilter),)


admin.site.register(User)
