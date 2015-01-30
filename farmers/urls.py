from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'farmers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^checkout$', CheckoutPageView.as_view(), name='checkout'),
    url(r'^init$', InitView.as_view(), name='init'),

)
