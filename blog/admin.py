from django.contrib import admin

from blog.models import Post, Category, PostCategory, PostTag, Newsletter, PostComment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('name', 'name_en')
    prepopulated_fields = {"slug": ('name_en',)}


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 3


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('author', 'title', 'title_en', 'body')
    prepopulated_fields = {"slug": ('title_en',)}
    inlines = (PostCategoryInline, PostTagInline)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    list_filter = ('is_active',)


class PostCommentParentInline(admin.StackedInline):
    model = PostComment
    extra = 1

    def get_fields(self, request, obj=None):
        return super().get_fields(request, obj)


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'parent', 'is_active', 'is_read', 'is_child')
    list_filter = ('is_active', 'is_read', 'is_child')
    list_editable = ('is_active', 'is_read')
    search_fields = ('fullname', 'post__title', 'post__body', 'website', 'body', 'parent__fullname', 'parent__body')
    inlines = (PostCommentParentInline,)



