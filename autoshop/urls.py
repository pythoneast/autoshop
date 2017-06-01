"""autoshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from autoshop import views
from autoshop.users import views as sign_views
from autoshop.products import views as products_views

urlpatterns = [
    url(r'^$', views.index, name='index-main'),
    url(r'^admin/', admin.site.urls),
    url(r'^cart/$', TemplateView.as_view(template_name="products/cart.html"), name='cart'),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^products/', include('autoshop.products.urls')),
    url(r'^catalog/', include('autoshop.categories.urls')),
    url(r'^sign-in/$', sign_views.signin, name='signin'),
    url(r'^sign-up/$', sign_views.signup, name='signup'),
    url(r'^sign-out/$', sign_views.signout, name='signout'),
    url(r'^items/$', products_views.get_products_by_ajax, name='product-ajax')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
