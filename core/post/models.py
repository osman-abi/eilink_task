"""Post and Comment models
These models (MPTTModel, TreeForeignKey) are used for to build hierarchical comment system
"""
from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from account.models import User

# pylint: disable=R0903
# Create your models here.


class Post(models.Model):
    """Post model's fields"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    vote_count = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.title)


class Comment(MPTTModel):
    """We are using MPTTModel to create hierarchical comment structure"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name="children"
    )
    content = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


    def __str__(self):
        return str(self.content)

    class MPTTMeta:
        """ordering by creating date in structure"""

        order_insertion_by = ["creation_date"]
