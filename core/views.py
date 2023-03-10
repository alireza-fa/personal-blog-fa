from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import FormView

from core.forms import ContactForm
from blog.models import Post
from blog.forms import NewsletterForm


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
        string = render_to_string('core/ajax/contact_success_form.html', {"form": form})
        return JsonResponse(data={"data": string, "status": 'ok'})

    def form_invalid(self, form):
        string = render_to_string('core/ajax/contact_form.html', {"form": form})
        return JsonResponse(data={"data": string, "status": 'bad'})


class NewsletterPartialView(FormView):
    template_name = 'include/newsletter.html'
    form_class = NewsletterForm

    def get_context_data(self, **kwargs):
        return {"news_form": self.get_form()}

    def form_valid(self, form):
        form.save()
        string = render_to_string('core/ajax/newsletter_success.html', {"news_form": self.form_class()})
        return JsonResponse(data={"data": string, "status": 'ok'})

    def form_invalid(self, form):
        string = render_to_string('core/ajax/newsletter.html', {"news_form": form})
        return JsonResponse(data={"data": string, "status": 'bad'})
