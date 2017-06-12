from django.conf.urls import url
from .views import home_view

app_name = 'framework'

urlpatterns = [
    url(r'^$', home_view, name='home'),
]
