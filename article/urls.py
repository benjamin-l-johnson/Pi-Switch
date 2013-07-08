from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^all/$' , 'article.views.articles'),
		url(r'^(?P<article_id>\d+)/$', 'article.views.article'),
		url(r'^all/$' , 'article.views.articles'),
		url(r'^search/$', 'article.views.buttonPush'),
		url(r'^about/$', 'article.views.about'),
		url(r'^contact/$', 'article.views.contact'),

		#url(r'^language/(?P<language>[a-z\-]+)/$',article,views,language),

)