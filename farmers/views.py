from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'base.html'

class CheckoutPageView(TemplateView):
	template_name = 'checkout.html'

class InitView(TemplateView):
	template_name = 'init.html'


