from django.conf.urls import url
from .views import list_view

app_name = 'faq'

urlpatterns = [
    # url(r'^(?P<tag>#[\w-]+)$', list_view, name='list'),
    url(r'^$', list_view, name='list'),
]
