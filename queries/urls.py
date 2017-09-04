from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from queries import views

urlpatterns = [
    url(r'^queries/$', views.QueryList.as_view(), name='queries-list'),
    url(r'^queries/(?P<pk>[0-9]+)/$', views.QueryDetail.as_view(), name='query-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
