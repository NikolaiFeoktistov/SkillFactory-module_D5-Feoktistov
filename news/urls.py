from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:news_id>/', views.news_detail, name='news_detail'),
    path('search/', views.news_search, name='news_search'),
    path('add/', views.news_create, name='news_create'),
    path('<int:news_id>/edit/', views.news_edit, name='news_edit'),
    path('<int:news_id>/delete/', views.news_delete, name='news_delete'),
]
