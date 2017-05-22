from django.conf.urls import url
from queries import views

urlpatterns = [
    url(r'^queries/$', views.query_list),
    url(r'^queries/(?P<pk>[0-9]+)/$', views.query_detail),
]
