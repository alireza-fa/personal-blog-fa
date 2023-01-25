from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.urls import reverse_lazy

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
        string = render_to_string('blog/ajax/comment_form.html', {"form": form})
        return JsonResponse(data={"data": string})

    def form_valid(self, form):
        form.save(post=self.get_object())
        string = render_to_string('blog/ajax/comment_success_form.html', {"form": self.form_class()})
        return JsonResponse(data={"data": string})


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


class PostSearchView(ListView):
    template_name = 'blog/post_search.html'
    paginate_by = 10

    def get_search_word(self):
        return self.request.GET.get('search')

    def get_queryset(self):
        search_word = self.get_search_word()
        if search_word:
            posts = Post.objects.filter(
                Q(title__icontains=search_word) | Q(title_en__icontains=search_word) |
                Q(introduction__icontains=search_word) | Q(body__icontains=search_word) |
                Q(categories__category__name__icontains=search_word)
            ).distinct()
            return posts
        return Post.objects.all()

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        search_word = self.get_search_word()
        if search_word:
            context['search_word'] = search_word
        return context
