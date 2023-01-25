from django import template

from blog.models import Post, Category
from core.models import InstagramPost


register = template.Library()


def get_new_posts():
    return Post.objects.all()[:3]


def get_tags():
    return Category.objects.all()


def get_instagram_posts():
    return InstagramPost.objects.all()[:6]


@register.filter(name='sidebar')
def sidebar_filter(value):
    filter_dict = {
        "new_posts": get_new_posts,
        "categories": get_tags,
        'instagram_posts': get_instagram_posts,
    }
    func = filter_dict.get(value)
    if func:
        return func()
