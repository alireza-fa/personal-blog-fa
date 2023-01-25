from django.urls import path

from blog import views


app_name = 'blog'
urlpatterns = [
    path('post/detail/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/category/<slug:slug>/', views.PostCategoryView.as_view(), name='post-category'),
    path('post/search/', views.PostSearchView.as_view(), name='post-search'),
]
