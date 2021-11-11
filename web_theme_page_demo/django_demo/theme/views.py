from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from theme.models import Theme, Place


# Create your views here.
class ThemeDV(DetailView):
    model = Theme
    template_name = 'theme/theme_detail.html'
    context_object_name = 'themes'

class PlaceDV(DetailView):
    model = Place
    template_name = 'theme/place_detail.html'
    context_object_name = 'places'