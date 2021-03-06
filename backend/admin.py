from django.contrib import admin
from .models import User

class UserAdminView(admin.ModelAdmin):
    list_display= ('id','first_name', 'last_name', 'email')

admin.site.register(User, UserAdminView)
