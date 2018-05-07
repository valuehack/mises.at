from django.conf.urls import url
from .views import list_view, detail_view

app_name = 'projekte'

urlpatterns = [
    url(r'^$', list_view, name='list'),
    url(r'^(?P<projekt_slug>[\w-]+)/$', detail_view, name='detail'),
]
