

from django.conf.urls import url

from products.views import ProductListView, ProductSlugDetailView
urlpatterns = [
    url(r'^$',ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$',ProductSlugDetailView.as_view(), name='detail'),
    #url(r'^products-fbv/$',product_list_view),
    #url(r'^products/(?P<pk>\d+)/$',ProductDetailView.as_view()),
    
    #url(r'^products-fbv/(?P<pk>\d+)/$',product_detail_view),
    #url(r'^featured/$',ProductFeaturedListView.as_view()),
    #url(r'^featured/(?P<pk>\d+)/$',ProductFeaturedDetailView.as_view()),
]

