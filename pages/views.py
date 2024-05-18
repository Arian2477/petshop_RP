from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from products.models import Product


class HomePageView(generic.ListView):
    model = Product
    template_name = 'Home.html'
    context_object_name = 'products'


class AboutUsPageView(TemplateView):
    template_name = 'pages/about_us.html'
