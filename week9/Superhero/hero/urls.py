"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from hero.hero_views import IndexView, HeroListView, HeroDetailView, HeroAddView, HeroEditView, HeroDeleteView
from hero.article_views import ArticleCreateView, ArticleDeleteView, ArticleDetailView,ArticleListView,ArticleUpdateView
from django.urls import path
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib.auth import logout



urlpatterns = [
   
    

    path('logout', logout, name='logout'),
    path('', IndexView.as_view()),
    path('hero/', HeroListView.as_view(), name = 'hero_list'),
    path('hero/<int:pk>', HeroDetailView.as_view(), name = 'hero_detail'),
    path('hero/add', HeroAddView.as_view(), name = 'hero_add'),
    path('hero/<int:pk>/', HeroEditView.as_view(), name = 'hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(), name = 'hero_delete'),

        # Article
    path('article/',                   ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',           ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',                ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/',          ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete',    ArticleDeleteView.as_view(),  name='article_delete'),
]
