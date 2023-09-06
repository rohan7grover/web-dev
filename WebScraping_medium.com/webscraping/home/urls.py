from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('scraper', views.scraper, name='scraper'),
    path('blog', views.blog, name='blog')
]