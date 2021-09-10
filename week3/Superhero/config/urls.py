from django.urls import path
from Hero.views import HulkView, IronManView, BlackWidowView

urlpatterns = [
    path('hulk', HulkView.as_view()),
    path('ironman',IronManView.as_view()),
    path('blackwidow', BlackWidowView.as_view()),
]