from django.contrib import admin
from .models import Conversation, ConversationMessage


class ConversationAdmin(admin.ModelAdmin):
    # Display specific columns to show in the panel
    list_display = ("item", "show_members", "created_at", "modified_at")

    # readonly fields to show in the panel
    readonly_fields = ('created_at', 'modified_at')

    def show_members(self, obj):

        return '-'.join([member.username for member in obj.members.all()])

    show_members.short_description = 'Members'


admin.site.register(Conversation, ConversationAdmin)


class ConversationMessageAdmin(admin.ModelAdmin):
    # Display specific columns to show in the panel
    list_display = ("conversation", "sender", "message", "created_at", "read")

    # readonly fields to show in the panel
    readonly_fields = ('created_at',)


admin.site.register(ConversationMessage, ConversationMessageAdmin)
