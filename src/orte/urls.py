from django.conf.urls import url
from .views import map_view, detail_view

app_name = 'orte'

urlpatterns = [
    url(r'^(?P<ort_slug>[\w-]+)/$', detail_view, name='detail'),
    url(r'^$', map_view, name='map'),
]
