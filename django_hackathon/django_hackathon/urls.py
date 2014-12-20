from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'core.views.home', name='home'),

    #Authentication views
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'registration/login.html'},
    name='login'),

    url(r'^admin/', include(admin.site.urls)),
)
