from django.urls import path
from . import views

urlpatterns = [
    path('<str:CAT_INPUT>/<str:SLUG_INPUT>/', views.blog, name='blog'),
    path('<str:CAT_INPUT>/', views.category, name='category'),
    path('', views.index, name='blog_index'),
]
