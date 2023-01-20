from django.contrib import admin

from core.models import AboutMe, Contact, Advertisement, InstagramPost, Tag


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'address')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'subject', 'is_read', 'is_active', 'created')
    list_filter = ('is_active', 'is_read')
    list_editable = ('is_active', 'is_read')
    search_fields = ('fullname', 'email', 'subject', 'message')


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('name', 'expired_at', 'image')
    search_fields = ('name',)


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'image')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
