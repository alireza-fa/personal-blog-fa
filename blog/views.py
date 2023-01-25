from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from blog.models import Post, Category
from blog.forms import PostCommentForm


class PostDetailView(DetailView, FormView):
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    queryset = Post.objects.all()
    form_class = PostCommentForm

    def get_success_url(self):
        return reverse_lazy('blog:post-detail', args=(self.kwargs.get('slug')))

    def form_invalid(self, form):
        messages.error(self.request, _('Please filled form with correct information'))
        return render(self.request, self.template_name, {"object": self.get_object(), "form": form})

    def form_valid(self, form):
        form.save(post=self.get_object())
        messages.success(self.request, _('Your comment Sent successfully'))
        return render(self.request, self.template_name, {"object": self.get_object(), "form": self.form_class()})


class PostCategoryView(ListView):
    template_name = 'blog/category.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    paginate_by = 10

    def get_category(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return category

    def get_queryset(self):
        return Post.objects.filter(categories__category=self.get_category())

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['category'] = self.get_category()
        return context
