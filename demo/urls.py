from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    (r'^moneybookers/status_url/', include('moneybookers.urls')),
    url(r'', include('demo.urls')),
)
