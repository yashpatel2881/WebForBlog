from django.contrib import admin
from . models import Post
from django.contrib.auth.models import User

# Admin panel customization.

admin.site.site_header = "Blog Site - Admin"
admin.site.site_title = "Blog Admin Poratl"
admin.site.index_title = "Welcome Admin"

class AdminPost(admin.ModelAdmin):

    list_display = ('Name','title', 'desc', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'date')

    fields = (
        'date',
        'title',
        'desc',
        'user'
    )

    def Name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

# Register your models here.

admin.site.register(Post, AdminPost)