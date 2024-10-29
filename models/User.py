""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class User(Model):
    """User Model"""

    @has_many("id", "user_id")
    def posts(self):
        from .Post import Post
         # id is the primary key in the users table
        # user_id is the column in the posts table referencing the users table record

        return Post
    

    @has_many("id", "user_id")
    def comments(self):
        from .Comment import Comment

        return Comment
