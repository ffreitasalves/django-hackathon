from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'core.views.home', name='home'),

    #Authentication views
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'registration/login.html',},
    name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page':'home'},name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
