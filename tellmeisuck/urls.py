from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tellmeisuck.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.login', name='login'),
    url(r'^display_friends/', 'main.views.display_friends', name='display_friends'),
    url(r'^create_user/', 'main.views.create_user', name = 'create_user'),
)
