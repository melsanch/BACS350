from django.urls import path
from Hero.views import IndexView, HeroDetailView, HeroListView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('hero/', HeroListView.as_view()),
    path('hero/<int:pk>', HeroDetailView.as_view()),
]