from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^denker/', include('denker.urls')),
    url(r'^literatur/', include('literatur.urls')),
    url(r'^orte/', include('orte.urls')),
    url(r'^verlag/', include('verlag.urls')),
    url(r'^projekte/', include('projekte.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^', include('framework.urls')),
]
