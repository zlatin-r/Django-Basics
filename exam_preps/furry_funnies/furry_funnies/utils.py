from author.models import Author
from posts.models import Post


def get_author_obj():
    return Author.objects.first()


def get_all_posts_obj():
    return Post.objects.all()
