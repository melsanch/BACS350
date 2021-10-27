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
from hero.views import IndexView, HeroListView, HeroDetailView, HeroAddView, HeroEditView, HeroDeleteView
from django.urls import path
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib.auth import logout



urlpatterns = [
    path('admin/', admin.site.urls),
        # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('doc.urls')),
    
    path('logout', logout, name='logout'),
    path('', IndexView.as_view()),
    path('hero/', HeroListView.as_view(), name = 'hero_list'),
    path('hero/<int:pk>', HeroDetailView.as_view(), name = 'hero_detail'),
    path('hero/add', HeroAddView.as_view(), name = 'hero_add'),
    path('hero/<int:pk>/', HeroEditView.as_view(), name = 'hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(), name = 'hero_delete'),
]
