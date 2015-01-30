from django.views.generic.base import TemplateView
from farmers.models import Product
from django.http import HttpResponse
from django.template import RequestContext, loader


class HomePageView(TemplateView):
    template_name = 'base.html'

    cat = category
    everything = Product.objects.all()
    prodSet = []
    for produce in everything:
        if produce.category == cat:
            if len(produce.getFarmers(date)) >= 1:
                prodSet.append(produce)
    return HttpResponse(prodSet)





