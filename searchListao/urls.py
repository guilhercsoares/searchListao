from django.conf.urls import patterns, include, url
from django.contrib import admin
from search import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'searchListao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
	url(r'^search/', views.index),
	url(r'^result/', views.result),
	url(r'^contato/', views.contact),
)
