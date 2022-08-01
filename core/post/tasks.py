"""In this file we create a task for reset Post vote count"""
from celery import shared_task
from .models import Post


@shared_task
def reset_post_vote():
    """We're filtering all posts which vote count greater than 0"""
    Post.objects.filter(vote_count__gt=0).update(vote_count=0)
    return {"response": "Task was successfully finished"}
