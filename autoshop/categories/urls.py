from django.conf.urls import url
from autoshop.categories import views


urlpatterns = [
    url(r'^(?P<cat_id>\d+)/$', views.cat_list, name='cat_list'),
    url(r'^(?P<cat_id>\d+)/(?P<subcat_id>\d+)/$', views.subcat_list, name='subcat_list'),
]