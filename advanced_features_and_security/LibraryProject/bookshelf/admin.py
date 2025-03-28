from django.contrib import admin
from .models import Book ,CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin
from .models import Post


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
admin.site.register(CustomUser, CustomUserAdmin)


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)