from django.contrib import admin
from .models import Memories


@admin.register(Memories)
class MemoriesAdmin(admin.ModelAdmin):
    """
    Add fields for Memories in admin panel
    """
    list_display = ('created_on', 'author', 'image', 'content', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['author', 'created_on']
    actions = ['approve_memory']

    def approve_memory(self, request, queryset):
        queryset.update(approved=True)
