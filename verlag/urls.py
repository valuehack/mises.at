from django.conf.urls import url
from .views import list_view

app_name = 'verlag'

urlpatterns = [
    url(r'^$', list_view, name='list'),
]
