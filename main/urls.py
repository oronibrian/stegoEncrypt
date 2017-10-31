
from django.conf.urls import url
from main.views import index, helpfunc

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^help/$', helpfunc, name='help'),

    ]
