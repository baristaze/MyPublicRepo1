from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GreenBox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^contact/?$', 'django.contrib.staticfiles.views.serve', kwargs={'path': './html/contact.html', 'document_root': settings.STATIC_ROOT}),	
    url(r'^welcome/?$', 'django.contrib.staticfiles.views.serve', kwargs={'path': './html/welcome.html', 'document_root': settings.STATIC_ROOT}),
)

