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
from django.urls import path

from accounts.views import AccountDeleteView, AccountDetailView, AccountListView, AccountCreateView, AccountUpdateView, SignUpView

urlpatterns = [

    # Account Views
    path('',                   AccountListView.as_view(),    name='account_list'),
    path('<int:pk>',           AccountDetailView.as_view(),  name='account_detail'),
    path('add',                AccountCreateView.as_view(),  name='account_add'),
    path('<int:pk>/',          AccountUpdateView.as_view(),  name='account_edit'),
    path('<int:pk>/delete',    AccountDeleteView.as_view(),  name='account_delete'),

    # Sign Up
    path('signup/', SignUpView.as_view(), name='signup'),
]