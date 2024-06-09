from django.db.models import Count
from django.shortcuts import render

from django.views.generic.base import TemplateView

from product_module.models import Product , ProductCategory
from site_module.models import SiteSetting, Slider
from utils.convertors import group_list


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        most_visited_products = Product.objects.filter(is_active=True, is_delete=False).annotate(visit_count=Count('productvisit')).order_by('-visit_count')[:12]
        context['latest_products'] = group_list(latest_products, 4)
        context['most_visited_products'] = group_list(most_visited_products,4)
        categories = list(ProductCategory.objects.annotate(products_count=Count('product_categories')).filter(is_active=True,is_delete=False,products_count__gt=0)[:6])
        categories_products= []
        for category in categories:
            item = {
                'id':category.id,
                'title':category.title,
                'products':(category.product_categories.all())
            }
            categories_products.append(item)

        context['categories_products'] = categories_products
        return context


def site_header_component(request):
    context = {

    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):

    context = {

    }
    return render(request, 'shared/site_footer_component.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context

