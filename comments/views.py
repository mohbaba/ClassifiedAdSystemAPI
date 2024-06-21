from django.db.migrations import serializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from ads.models import Ad
from models import Comment
from rest_framework.decorators import api_view
from serializers import CommentSerializer
from users.models import User


@api_view()
def comment_on_post(request, ad_id):
    ads = Ad.objects.get(pk=ad_id)
    comment = Comment.objects.create(ad_id, Comment.content)
    serializer = CommentSerializer(comment, many=True)
    serializer.save(comment)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def delete_comment(request, ad_id, content):
    comment_content = Comment.objects.get(content, ad_id)
    if request.User == comment_content.commenter:
        comment_content.delete()
        return HttpResponse("Comment deleted successfully")

@api_view()
def reply_comment(request, ad_id, content):
    comment = Comment.objects.get(ad_id, content)
    if request.User == comment.content:
        comment.save(content)
        return Response(serializer.data, status=status.HTTP_200_OK)


