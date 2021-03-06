from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from mysite import views
from mysite.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='publicIndex'),
    # Login / logout.
    url(r'^login/$', custom_login, name='login_page'),
    url(r'^logout/$', logout_page),
    url(r'^polls/',include('polls.urls', namespace='polls')),
    url(r'^users/',include('users.urls', namespace='users')),
    url(r'^users/messages/', include('django_messages.urls')),
    url(r'^notifications/', include('notification.urls')),
    #url(r'^xmlrpc$', 'rpc4django.views.serve_rpc_request'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    
    url(r'', include('django.contrib.flatpages.urls')),
   
    
    
    
)
