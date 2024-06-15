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


class SearchListView(generic.ListView):
    model = Product
    paginate_by = 10
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(SearchListView, self).get_queryset()
        if self.request.method == 'GET':
            query_name = self.request.GET.get('search_input')
            if query_name:
                queryset = Product.objects.filter(active=True).filter(title__contains=query_name)
                return queryset
            else:
                return queryset
