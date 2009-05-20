from django.conf.urls.defaults import *
from views import *

# Uncomment the next two lines to enable the admin:
# from cobbler_web.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^cobbler_web/$', index),
    (r'^cobbler_web/ksfile/list(/(?P<page>\d+))?$', ksfile_list),
    (r'^cobbler_web/ksfile/edit$', ksfile_edit, {'editmode':'new'}),
    (r'^cobbler_web/ksfile/edit/(?P<ksfile_name>.+)$', ksfile_edit, {'editmode':'edit'}),
    (r'^cobbler_web/ksfile/save$', ksfile_save),
    (r'^cobbler_web/snippet/list(/(?P<page>\d+))?$', snippet_list),
    (r'^cobbler_web/snippet/edit$', snippet_edit, {'editmode':'new'}),
    (r'^cobbler_web/snippet/edit/(?P<snippet_name>.+)$', snippet_edit, {'editmode':'edit'}),
    (r'^cobbler_web/snippet/save$', snippet_save),
    #(r'^cobbler_web/(?P<what>\w+)/list(/(?P<page>\d+))?', list),
    (r'^cobbler_web/(?P<what>\w+)/list(/(?P<page>\d+))?', genlist),
    #(r'^cobbler_web/(?P<what>\w+)/modifylist/(?P<pref>[!\w]+)/(?P<value>\w+)', modify_list),
    (r'^cobbler_web/(?P<what>\w+)/addfilter/(?P<filter>.+)$', modify_filter, {'action':'add'}),
    (r'^cobbler_web/(?P<what>\w+)/removefilter/(?P<filter>.+)$', modify_filter, {'action':'remove'}),
    (r'^cobbler_web/(?P<what>\w+)/edit/(?P<obj_name>.+)$', generic_edit, {'editmode': 'edit'}),
    (r'^cobbler_web/(?P<what>\w+)/new$', generic_edit, {'editmode': 'new'}),

    # FIXME: copy/edit/rename should not be edit type actions

    #(r'^cobbler_web/(?P<what>\w+)/rename/(?P<obj_name>[^/]+)$', generic_rename),
    #(r'^cobbler_web/(?P<what>\w+)/rename/(?P<obj_name>[^/]+)/(?P<obj_newname>[^/]+)$', generic_rename),
    #(r'^cobbler_web/(?P<what>\w+)/(?P<multi_mode>[\w\-]+)/multi$', generic_multi),
    #(r'^cobbler_web/(?P<what>\w+)/(?P<multi_mode>[\w\-]+)/domulti$', generic_domulti),
    #(r'^cobbler_web/distro/edit$', distro_edit),
    #(r'^cobbler_web/distro/edit/(?P<distro_name>.+)$', distro_edit),
    #(r'^cobbler_web/distro/save$', distro_save),
    #(r'^cobbler_web/profile/edit$', profile_edit),
    #(r'^cobbler_web/profile/edit/(?P<profile_name>.+)$', profile_edit),
    #(r'^cobbler_web/subprofile/edit$', profile_edit, {'subprofile': 1}),
    #(r'^cobbler_web/profile/save$', profile_save),
    #(r'^cobbler_web/system/edit$', system_edit),
    #(r'^cobbler_web/system/edit/(?P<system_name>.+)$', system_edit, {'editmode': 'edit'}),
    #(r'^cobbler_web/system/save$', system_save),
    #(r'^cobbler_web/network/edit$', network_edit),
    #(r'^cobbler_web/network/edit/(?P<network_name>.+)$', network_edit),
    #(r'^cobbler_web/network/save$', network_save),
    #(r'^cobbler_web/repo/edit$', repo_edit),
    #(r'^cobbler_web/repo/edit/(?P<repo_name>.+)$', repo_edit),
    #(r'^cobbler_web/repo/save$', repo_save),
    #(r'^cobbler_web/image/edit$', image_edit),
    #(r'^cobbler_web/image/edit/(?P<image_name>.+)$', image_edit),
    #(r'^cobbler_web/image/save$', image_save),
    (r'^cobbler_web/random_mac$', random_mac),
    (r'^cobbler_web/random_mac/virttype/(?P<virttype>.+)$', random_mac),
    (r'^cobbler_web/settings$', settings),
    (r'^cobbler_web/sync$', dosync),
    (r'^cobbler_web/(?P<what>\w+)/edit$', generic_edit),
    (r'^cobbler_web/(?P<what>\w+)/edit/(?P<obj_name>.+)$', generic_edit, {'editmode': 'edit'}),
    (r'^cobbler_web/(?P<what>\w+)/save$', generic_save),
)