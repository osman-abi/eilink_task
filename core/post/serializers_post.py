"""This file builds serializers for creating APIs"""
from rest_framework import serializers
from .models import Post

# pylint: disable=W0223
# pylint: disable=R0903

class PostSerializer(serializers.ModelSerializer):
    """This class is used to build serializer for Post model"""
    author = serializers.SerializerMethodField()

    class Meta:
        """This class is used to initialize model and fields"""
        model = Post
        fields = "__all__"

    def get_author(self, obj):
        """This function is used for getting name of auhtor"""
        return obj.author.username
