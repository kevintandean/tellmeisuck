from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tellmeisuck.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.login', name='login'),
    url(r'^display_friends/$', 'main.views.display_friends', name='display_friends'),
    url(r'^create_user/$', 'main.views.create_user', name = 'create_user'),
    url(r'^post/$', 'main.views.post', name = 'post'),
    url(r'^get_post/(?P<user_id>\w+)/$', 'main.views.get_post', name = 'get_post'),
    url(r'^check_new_post/(?P<user_id>\w+)/(?P<post_id>\w+)/$', 'main.views.check_new_post',name = 'check_new_post'),
    url(r'^user/(?P<user_id>\w+)/$', 'main.views.login_redirect', name="login_redirect")
)
