from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frosh.views.home', name='home'),
    # url(r'^frosh/', include('frosh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'directory.views.index'),
    #url(r'^index/$', 'directory.views.index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/edit/'}),
    url(r'^faq/$', 'directory.views.faq'),
    url(r'^sponsors/$', 'directory.views.sponsors'),
    url(r'^propaganda/$', 'directory.views.propaganda'),
    url(r'^houses/$', 'directory.views.houses'),
    url(r'^faq/$', 'directory.views.faq'),
    url(r'^register/$', 'directory.views.register'),
    url(r'^edit/$', 'directory.views.edit'),
    url(r'^houseLookup/$', 'directory.views.houseLookup'),
    url(r'^vassalLookup/$', 'directory.views.vassalLookup'),
    url(r'^vassalEdit/(\d+)/$', 'directory.views.vassalEdit'),
    url(r'^imageForm/(\d+)/$', 'directory.views.imageForm'),
    url(r'^imageUpload/(\d+)/$', 'directory.views.imageUpload'),
    url(r'^houseRetrieve/(\d+)/$', 'directory.views.houseRetrieve'),
 
                       
    
    
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
