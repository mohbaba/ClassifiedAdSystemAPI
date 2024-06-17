from django.contrib import admin

from messaging.models import Message

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'time_sent']
    search_fields = ['sender', 'receiver', 'time_sent']
