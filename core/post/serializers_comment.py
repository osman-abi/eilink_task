"""This file builds serializers for creating APIs"""
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    SerializerMethodField,
)
from .models import Comment

# pylint: disable=W0223
# pylint: disable=R0903

class RecursiveField(Serializer):
    """This class is used to structure Comment's children as hierarchical"""
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentSerializer(ModelSerializer):
    """This class is used to build serializer for comment"""

    children = RecursiveField(many=True)
    author = SerializerMethodField()

    class Meta:
        """This class is used to initialize model and fields"""
        model = Comment
        fields = [
            "id",
            "author",
            "post",
            "content",
            "creation_date",
            "parent",
            "children",
        ]

    def get_author(self, obj):
        """This function is used for getting name of auhtor"""
        return obj.author.username


class CommentCreateSerializer(ModelSerializer):
    """This class is used for only creating and updating APIs"""
    class Meta:
        """This class is used to initialize model and fields"""
        model = Comment
        fields = "__all__"
