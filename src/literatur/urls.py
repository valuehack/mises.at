from django.conf.urls import url
from .views import list_view, denker_view

app_name = 'literatur'

urlpatterns = [
    url(r'^(?P<denker_slug>[\w-]+)/$', denker_view, name='denker'),
    url(r'^$', list_view, name='list'),
]
