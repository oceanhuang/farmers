from django.views.generic.base import TemplateView
from farmers.models import Product
from django.http import HttpResponse
from django.template import RequestContext, loader


class HomePageView(TemplateView):
    template_name = 'base.html'

    


class CheckoutPageView(TemplateView):
	template_name = 'checkout.html'

class InitView(TemplateView):
	template_name = 'init.html'


