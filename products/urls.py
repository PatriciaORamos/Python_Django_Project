from django.conf.urls import url
from .import views

app_name='products'

urlpatterns = [
    url(r'^$', views.product_list, name="list"),
    url(r'^create/$', views.product_create, name="create"),
    url(r'^edit/(?P<pk>\d+)$', views.product_edit, name="edit"),
    url(r'^delete/(?P<pk>\d+)$', views.product_delete, name="delete"),
    url(r'^(?P<id>[0-9]+)/$', views.product_detail, name="detail"),
]
