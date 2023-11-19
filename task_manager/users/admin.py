from django.contrib import admin
from django.contrib.auth.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined')
    search_user = ['username', 'first_name', 'last_name']
    list_filter = (('date_joined', admin.DateFieldListFilter),)

#admin.site.register(User)
