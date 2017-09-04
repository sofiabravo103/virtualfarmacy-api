from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from queries import views

urlpatterns = [
    url(r'^queries/$', views.query_list),
    url(r'^queries/(?P<pk>[0-9]+)/$', views.query_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
