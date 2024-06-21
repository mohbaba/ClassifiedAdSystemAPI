from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializers):
    class Meta:
        model = Comment
        fields = ['post_id', 'commenter', 'content', 'time_of_comment', 'ad']