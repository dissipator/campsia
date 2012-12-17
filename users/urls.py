from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
    url(r'^attendance/$', views.attendance, name='attendance'),
    url(r'^notifications/$', views.notifications, name='notification'),
    url(r'^dues/$', views.dues, name='dues'),
    url(r'^inbox/$', views.inbox, name='inbox'),
)