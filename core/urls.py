from django.urls import path

from core import views


app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('newsletter/create/', views.NewsletterPartialView.as_view(), name='newsletter-create'),
]
