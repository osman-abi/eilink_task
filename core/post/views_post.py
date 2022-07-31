"""We create all CRUD Api"""
import json
import logging
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    DestroyAPIView,
    GenericAPIView,
)
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http.response import JsonResponse
from django.core.serializers import serialize
from .serializers_post import PostSerializer
from .models import Post

logger = logging.getLogger("django")

# Create your views here.
# pylint: disable=[C0103,W0702,W0613 ]


class PostCreateAPIView(CreateAPIView):
    """Create post"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)
        return super().perform_create(serializer)


class PostListAPIView(ListAPIView):
    """Get all posts"""

    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostRetrieveAPIView(RetrieveAPIView):
    """Get post detail info"""

    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "pk"


class PostUpdateAPIView(GenericAPIView, UpdateModelMixin):
    """Update the post's data"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "pk"

    def put(self, request, *args, **kwargs):
        """This method is used for execute mixins' update method"""
        response = self.update(request, *args, **kwargs)
        return response


class PostDestroyAPIView(DestroyAPIView):
    """Delete Post"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "pk"


class UpVoteAPIView(APIView):
    """Post's vote counting up"""

    permission_classes = [AllowAny]

    def post(self, request, pk):
        """In this method we get post via pk and then update its 'vote_count'"""
        try:
            post = Post.objects.get(pk=pk)
            post.vote_count += 1
            post.save()
            data = json.loads(serialize("json", Post.objects.filter(pk=pk)))
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse(
                {"fields": "errors", "message": f"Post cannot found with this id {pk}"}
            )


#####################################################################3

upvote_api = UpVoteAPIView.as_view()
post_create_api = PostCreateAPIView.as_view()
post_update_api = PostUpdateAPIView.as_view()
post_delete_api = PostDestroyAPIView.as_view()
post_detail_api = PostRetrieveAPIView.as_view()
post_list_api = PostListAPIView.as_view()
