"""URLs of 'post' application"""
from django.urls import path
from .views_post import (
    upvote_api,
    post_create_api,
    post_delete_api,
    post_detail_api,
    post_update_api,
    post_list_api,
)

from .views_comment import (
    comment_create_api,
    comment_list_api,
    comment_update_api,
    comment_delete_api,
)

urlpatterns = [
    # POST URLS
    path("upvote/<int:pk>/", upvote_api, name="upvote"),
    path("post-create/", post_create_api, name="post-create"),
    path("post-detail/<int:pk>/", post_detail_api, name="post-detail"),
    path("post-list/", post_list_api, name="post-list"),
    path("post-update/<int:pk>/", post_update_api, name="post-update"),
    path("post-delete/<int:pk>/", post_delete_api, name="post-delete"),
    # COMMENT URLS
    path("comment-list/", comment_list_api, name="comment-list"),
    path("comment-create/", comment_create_api, name="comment-create"),
    path("comment-update/<int:pk>/", comment_update_api, name="comment-update"),
    path("comment-delete/<int:pk>/", comment_delete_api, name="comment-delete"),
]
