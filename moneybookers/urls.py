from django.conf.urls.defaults import *

urlpatterns = patterns('moneybookers.views',
	url(r'^$', 'status', name="mb-status"),
)
