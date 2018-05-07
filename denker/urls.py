from django.conf.urls import url
from .views import detail_view, list_view

app_name = 'denker'

urlpatterns = [
    url(r'^(?P<denker_slug>[\w-]+)/$', detail_view, name='detail'),
    url(r'^$', list_view, name='list'),
]
