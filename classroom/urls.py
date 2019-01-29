from django.conf.urls import url
from . import views
from . import email

urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url('^index/$',views.index,name='index'),
    url(r'^signup/$', email.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',email.activate, name='activate'),
    url(r'^setprofile/$', views.setprofile, name='setprofile'),
    url(r'^student/$', views.student, name='student'),
    url(r'^teacher/$', views.teacher, name='teacher'),
    url(r'^administrator/$', views.administrator, name='administrator'),
]
