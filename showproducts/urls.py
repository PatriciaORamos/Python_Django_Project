from django.conf.urls import url
from .import views

app_name='showproducts'

urlpatterns = [
    url(r'^$', views.showproduct_list, name="list"),
    url(r'^(?P<id>[0-9]+)/$', views.showproduct_detail, name="detail"),
]
