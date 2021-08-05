from django.urls import path
from .views import AboutPageView, HomePageView, MyAppView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('app/', MyAppView.as_view(), name="app"),
    path('about/', AboutPageView.as_view(), name="about"),
]