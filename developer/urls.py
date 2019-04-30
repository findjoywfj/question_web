from django.conf.urls import url
from developer.views import home,\
                            admin_qes_delete_item,admin_qes_edit,\
                            admin_qes_action,\
                            admin_result_edit,\
                            admin_result_delete,admin_qes_edit_action,\
                            api_catalog_get,api_catalog_action, admin_record_get,admin_record_show
urlpatterns = [
    url(r'^$', home),
    url(r'^admin/delete/item/(?P<item_id>\w+)/$', admin_qes_delete_item),
    url(r'^admin/qes_body/edit/(?P<item_id>\w+)/$', admin_qes_edit),
    url(r'^admin/qes_body/action/(?P<query_id>\w+)/$', admin_qes_action),
    url(r'^qes_body/result_edit/(?P<query_id>\w+)/$', admin_result_edit),
    url(r'^qes_body/result_delete/(?P<query_id>\w+)/(?P<index>\d+)/$', admin_result_delete),
    url(r'^admin/qes_body/edit/action/(?P<item_id>\w+)/$',admin_qes_edit_action),
    url(r'^api/catalog/get/$', api_catalog_get),
    url(r'^api/catalog/action/$', api_catalog_action),
    url(r'^record/(?P<query_id>\w+)/$', admin_record_show),
    url(r'^api/record/get/$', admin_record_get)


]