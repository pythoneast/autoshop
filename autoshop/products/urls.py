from django.conf.urls import url
from autoshop.products import views


urlpatterns = [
    url(r'^details/(?P<id>\d+)/$', views.detail, name='product-detail'),
]
