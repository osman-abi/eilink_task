"""
In this file we're doing something
"""
import logging
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    GenericAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.mixins import UpdateModelMixin

from .serializers_comment import CommentSerializer, CommentCreateSerializer
from .models import Comment


logger = logging.getLogger("django")

""" We have to create class methods such as below for logging responses:
post(); put(); delete(); get();
"""

# Create
class CommentCreateAPIView(CreateAPIView):
    """create comment api class"""

    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


# Read
class CommentListAPIView(ListAPIView):
    """getting all comments"""

    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().filter(level=0)


# Update
class CommentUpdateAPIView(GenericAPIView, UpdateModelMixin):
    """update comment"""

    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()
    lookup_field = "pk"

    def put(self, request, *args, **kwargs):
        """this method is used for mixin action"""
        response = self.update(request, *args, **kwargs)
        return response


# Delete
class CommentDestroyAPIView(DestroyAPIView):
    """At this point we're deleting comment"""

    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = "pk"


##############################################################33
comment_create_api = CommentCreateAPIView.as_view()
comment_list_api = CommentListAPIView.as_view()
comment_update_api = CommentUpdateAPIView.as_view()
comment_delete_api = CommentDestroyAPIView.as_view()
