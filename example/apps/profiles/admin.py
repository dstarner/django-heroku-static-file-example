from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    autocomplete_fields = ('user',)

    list_display = ('user',)
