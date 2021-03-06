from django.contrib import admin
from django.conf.urls import url, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from products import views as products_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  
    url(r'^accounts/', include('accounts.urls') ),
    url(r'^categories/', include('categories.urls') ),
    url(r'^products/', include('products.urls') ),
    url(r'^showproducts/', include('showproducts.urls') ),
    url(r'^$', views.homepage, name="home" ),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)