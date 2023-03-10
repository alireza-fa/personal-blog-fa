from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class AboutMe(models.Model):
    first_name = models.CharField(max_length=34, verbose_name=_('first name'))
    first_name_en = models.CharField(max_length=34, verbose_name=_('first name english'))
    last_name = models.CharField(max_length=34, verbose_name=_('last name'))
    last_name_en = models.CharField(max_length=34, verbose_name=_('last name english'))
    position = models.CharField(max_length=120, verbose_name=_('position'))
    position_en = models.CharField(max_length=120, verbose_name=_('position english'))
    phone_number = models.CharField(max_length=18, verbose_name=_('phone number'))
    email = models.EmailField(max_length=120, verbose_name=_('email'))
    address = models.CharField(max_length=250, verbose_name=_('address'))
    describe = RichTextField(verbose_name=_('describe'))
    image_background = models.ImageField(
        verbose_name=_('image background'), default='medical_wall.jpg', help_text=_('recommended: Image(1920X1279)'))
    image_logo = models.FileField(verbose_name=_('image logo'), help_text=_('recommended: Image(format is .svg)'))
    image_about = models.ImageField(
        verbose_name=_('Image for about page'), help_text=_('recommended: Image(1680X1120)'))
    image_avatar1 = models.ImageField(
        verbose_name=_('Image for big avatar'), help_text=_('recommended: Image(100X100)'))
    image_avatar2 = models.ImageField(
        verbose_name=_('Image for medium avatar'), help_text=_('recommended: Image(80X80)')
    )
    image_avatar3 = models.ImageField(
        verbose_name=_('Image for small avatar'), help_text=_('recommended: Image(60X60)')
    )
    describe_short = models.TextField(max_length=250, verbose_name=_('describe short'))
    introduction = models.CharField(max_length=200, verbose_name=_('introduction'))
    facebook = models.CharField(max_length=120, verbose_name=_('facebook'), default='#')
    twitter = models.CharField(max_length=120, verbose_name=_('twitter'), default='#')
    instagram = models.CharField(max_length=120, verbose_name=_('instagram'), default='#')
    instagram_id = models.CharField(max_length=64, verbose_name=_('instagram id'))
    pinterest = models.CharField(max_length=120, verbose_name=_('pinterest'), default='#')
    youtube = models.CharField(max_length=120, verbose_name=_('youtube'), default='#')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('About Me')
        verbose_name_plural = _('About Me')

    def __str__(self):
        return self.get_fullname()

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def get_fullname_en(self):
        return f'{self.first_name_en} {self.last_name_en}'


class Contact(models.Model):
    fullname = models.CharField(max_length=34, verbose_name=_('fullname'))
    email = models.EmailField(max_length=120, verbose_name=_('email'))
    subject = models.CharField(max_length=120, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    is_read = models.BooleanField(default=False, verbose_name=_('is read'))
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.fullname


class InstagramPost(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    image = models.ImageField(verbose_name=_('image'))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Instagram Post')
        verbose_name_plural = _('Instagram Posts')

    def __str__(self):
        return self.name
