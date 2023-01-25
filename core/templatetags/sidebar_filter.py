from django import template

from blog.models import Post, Category


register = template.Library()


def get_new_posts():
    return Post.objects.all()[:3]


def get_tags():
    return Category.objects.all()


@register.filter(name='sidebar')
def sidebar_filter(value):
    filter_dict = {
        "new_posts": get_new_posts,
        "categories": get_tags,
    }
    func = filter_dict.get(value)
    if func:
        return func()
