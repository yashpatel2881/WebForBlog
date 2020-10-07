from django.contrib import admin
from django.contrib.auth.models import User
from . models import Profile


# Admin Panel Customization.

class AdminProfile(admin.ModelAdmin):

    list_display = ('User', 'Email')

    def User(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def Email(self, obj):
        return obj.user.email

# Register your models here.

admin.site.register(Profile, AdminProfile)