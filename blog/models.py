from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone
from A.local_settings import URL_ROOT

from ckeditor.fields import RichTextField

from blog.managers import IsActiveManager
from core.models import AboutMe


class Category(models.Model):
    name = models.CharField(max_length=34, verbose_name=_('name'))
    name_en = models.CharField(max_length=34, verbose_name=_('name english'))
    slug = models.SlugField(max_length=50, verbose_name=_('slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:post-category', args=(self.slug,))


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    title_en = models.CharField(max_length=120, verbose_name=_('title english'))
    slug = models.SlugField(max_length=150, verbose_name=_('slug'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name='posts', verbose_name=_('author'))
    body = RichTextField(verbose_name=_('body'))
    published_at = models.DateTimeField(default=timezone.now(), verbose_name=_('published at'))
    image_cover = models.ImageField(verbose_name=_('image_cover'), help_text=_('recommended: Image(550X367)'))
    image = models.ImageField(verbose_name=_('image'), help_text=_('recommended: Image(750X540)'))
    image_avatar = models.ImageField(verbose_name=_('image avatar'), help_text=_('recommended: Image(60X60)'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    default_manager = models.Manager()
    objects = IsActiveManager()

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return f'{self.author} - {self.title}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:post-detail', args=(self.slug,))

    @staticmethod
    def get_url_root():
        return URL_ROOT

    def get_post_link(self):
        return self.get_url_root() + self.get_absolute_url()

    @staticmethod
    def get_custom_text():
        return 'personal-blog-tina-montazeri'

    def get_facebook_share_link(self):
        facebook_share_link = 'https://www.facebook.com/sharer/sharer.php?u={}'
        return facebook_share_link.format(self.get_post_link())

    def get_twitter_share_link(self):
        twitter_share_link = 'https://twitter.com/intent/tweet?url={}&text={}'
        return twitter_share_link.format(self.get_post_link(), self.get_custom_text())

    def get_linkedin_share_link(self):
        linkedin_share_link = 'https://www.linkedin.com/shareArticle?mini=true&url={}&title={}'
        return linkedin_share_link.format(self.get_post_link(), self.get_custom_text())

    def get_pinterest_share_link(self):
        pinterest_share_link = 'https://www.pinterest.com/pin/find/?url={}&description={}'
        return pinterest_share_link.format(self.get_post_link(), self.get_custom_text())

    def get_tumble_share_link(self):
        tumble_share_link = 'http://www.tumblr.com/share?v=3&u={}&t={}'
        return tumble_share_link.format(self.get_post_link(), self.get_custom_text())

    def get_telegram_share_link(self):
        telegram_share_link = 'https://telegram.me/share/url?url={}&text={}'
        return telegram_share_link.format(self.get_post_link(), self.get_custom_text())

    def get_instagram_share_link(self):
        instagram_share_link = ''
        return '#'

    def get_google_plus_share_link(self):
        google_plus_share_link = 'https://plus.google.com/share?url={}'
        return google_plus_share_link.format(self.get_post_link())

    def get_whatsapp_share_link(self):
        whatsapp_share_link = 'whatsapp://send?text={}'
        return whatsapp_share_link.format(self.get_post_link())


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='categories', verbose_name=_('post'))
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='posts', verbose_name=_('category'))

    class Meta:
        verbose_name = _('Post Category')
        verbose_name_plural = _('Post Categories')

    def __str__(self):
        return f'{self.post} - {self.category}'


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags', verbose_name=_('post'))
    name = models.CharField(max_length=34, verbose_name=_('name'))

    class Meta:
        verbose_name = _('Post Tag')
        verbose_name_plural = _('Post Tags')

    def __str__(self):
        return f'{self.name} - {self.post}'


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name=_('post'), blank=True)
    fullname = models.CharField(max_length=34, verbose_name=_('fullname'), blank=True)
    email = models.EmailField(max_length=120, verbose_name=_('email'), blank=True)
    website = models.CharField(max_length=120, verbose_name=_('website'), null=True, blank=True)
    body = models.CharField(max_length=120, verbose_name=_('body'))
    image = models.ImageField(default='comment_avatar.png', verbose_name=_('image'))
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children', verbose_name=_('parent'), null=True, blank=True)
    is_child = models.BooleanField(default=False, verbose_name=_('is child'))
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))
    is_read = models.BooleanField(default=False, verbose_name=_('is read'))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    default_manager = models.Manager()
    objects = IsActiveManager()

    class Meta:
        verbose_name = _('Post Comment')
        verbose_name_plural = _('Post Comments')

    def __str__(self):
        return self.fullname

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.parent:
            me = AboutMe.objects.first()
            self.post = self.parent.post
            self.is_child = True
            self.fullname = me.get_fullname()
            self.image = me.image_avatar2
        return super().save()

    def get_parent_comment(self):
        return PostComment.objects.filter(is_child=False)

    def get_children(self):
        return self.children.filter(is_active=True)


class Newsletter(models.Model):
    email = models.EmailField(max_length=120, verbose_name=_('email'))
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))

    class Meta:
        verbose_name = _('Newsletter')
        verbose_name_plural = _('Newsletters')

    def __str__(self):
        return self.email
