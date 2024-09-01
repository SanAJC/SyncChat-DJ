from django.contrib import admin
from .models import Chat, Message, ChatParticipant


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_group')
    search_fields = ('name',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'user', 'content', 'time')
    list_filter = ('chat', 'time')
    search_fields = ('content',)

@admin.register(ChatParticipant)
class ChatParticipantAdmin(admin.ModelAdmin):
    list_display = ('chat', 'user')
    list_filter = ('chat',)
    search_fields = ('chat__name', 'user__username')

