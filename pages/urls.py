from django.conf.urls import url
from .views import *

app_name = "pages"

urlpatterns = [

    url(r'^hakkimizda/$', hakkimizda, name="hakkimizda"),

    url(r'^iletisim/$', iletisim, name='iletisim'),
]
