from django.contrib import admin
from .models import UserProfile


#admin.site.register(UserProfile)


class UserProfileAdmin(admin.ModelAdmin):
    list_display=('timestamp ','updated','is_active')
admin.site.register(UserProfile)