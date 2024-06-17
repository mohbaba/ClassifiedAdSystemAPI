from django.contrib import admin

from comments.models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'commenter', 'content', 'time_of_comment', 'ad']
    search_fields = ['id', 'commenter', 'content', 'time_of_comment', 'ad']