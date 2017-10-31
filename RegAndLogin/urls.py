from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   # url(r'^loginpage/$',views.login, name='loginpage'),

    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', auth_views.logout,name='logout'),
    url(r'^registerpage/$', views.Register_view, name='registerpage'),



]
