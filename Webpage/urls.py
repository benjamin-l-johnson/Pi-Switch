from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^articles/' , include('article.urls')),
    #url(r'^hello/$', 'article.views.Hello'),
    #url(r'^hello_template/$', 'article.views.hello_template'),
    # url(r'^Webpage/', include('Webpage.foo.urls')),
    
    #login stuff
		url(r'^accounts/login/$', 'Webpage.views.login'),
		url(r'^accounts/auth/$', 'Webpage.views.auth_view'),
		url(r'^accounts/logout/$', 'Webpage.views.logout'),
    url(r'^accounts/loggedin/$', 'article.views.articles'),
    url(r'^accounts/invalid/$', 'Webpage.views.invalid_login'),
     
    #user accounts register stuff
	
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
