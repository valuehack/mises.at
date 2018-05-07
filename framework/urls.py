from django.conf.urls import url
from .views import home_view
from django.http import HttpResponse

app_name = 'framework'

urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'^googlee50af1936941f141.html$', lambda request: HttpResponse('google-site-verification: googlee50af1936941f141.html'))
]
