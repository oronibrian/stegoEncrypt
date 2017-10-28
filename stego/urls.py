
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='userauth/login/', permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', include('main.urls',namespace='index')),
    url(r'^userauth/', include("RegAndLogin.urls", namespace='userauth')),

    ]
