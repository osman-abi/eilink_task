"""In this file we create a task for reset Post vote count"""
from celery import shared_task
from .models import Post
import logging
logger = logging.getLogger('celery')

@shared_task
def reset_post_vote():
    """We're filtering all posts which vote count greater than 0"""
    posts = Post.objects.filter(vote_count__gt=0)
    for post in posts:
        post.vote_count = 0
        post.save()
    return {"response": "Task was successfully finished"}
