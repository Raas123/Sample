from django.conf.urls import url, include
from . import views
#from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
	url(r'^creditcardenquiry/$', views.creditcardenquiry, name='creditcardenquiry'),
	url(r'^creditcardenquirylist/$', views.creditcardenquirylist, name='creditcardenquirylist'),
	url(r'^register/$', views.register, name='register'),
	#url(r'^creditcardenquirylist/update_list/(?P<list_id>\d+)/$', views.index, name='index'),
	url(r'^creditcardenquirylist/update_list/(?P<list_id>\d+)/$', views.index1, name='index1'),
]
