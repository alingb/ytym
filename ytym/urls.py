from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'ytym.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^technology/', include(admin.site.urls)),
    url(r'^data/file/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    url(r'^file/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/data/ftp/breakin/breakin-img' }),
    url(r'^bugsystem/$','technology.views.erro'),
    url(r'^faebugsystem/$','technology.views.faeErro'),
    url(r'technology/web/(?P<table>.*)/detail/(?P<id>.*)/(?P<mang>.*)$','web.views.usename'),
    url(r'web/detail/(?P<productName>.*)/$', "web.views.product"),
    url(r'web/product/$', "web.views.productCollect"),
    url(r'^smart/(?P<id>.*)$','web.views.smartid'),
    url(r'^web/collect/$','web.views.collect'),
    url(r'^status/$','web.views.form'),
    url(r'^status/page/$','web.views.form_page'),
    url(r'^$','web.views.index'),
    url(r'^mess/$','web.views.info'),
    url(r'^technology/smart/$','web.views.smart'),
    url(r'^login/$','technology.views.alogin'),
    url(r'^logout/$','technology.views.logout'),
    url(r'^check/$','web.views.checkStat'),
    url(r'^test/$','web.views.test'),
    url(r'^change_bios_bmc/$','web.views.change_bios_bmc'),
    url(r'^change_status/$','web.views.change_status'),
   
]
