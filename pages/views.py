from django.shortcuts import render
from django.views.generic import TemplateView


class MyAppView(TemplateView):
    template_name = "app.html"

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
