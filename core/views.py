from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.utils.translation import gettext_lazy as _

from core.forms import ContactForm
from blog.models import Post


class HomeView(ListView):
    template_name = 'core/home.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all()


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('successful'))
        return super().form_valid(form)
