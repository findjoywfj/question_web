from django.conf.urls import url
from developer.views import home,qes_show,admin_qes_add,admin_qes_delete,admin_qes_delete_item,admin_qes_edit,admin_qes_action,admin_query_rename,admin_query_add
urlpatterns = [
    url(r'^$', home),
    url(r'^qes_body/(?P<query_id>\d+)/$', qes_show),
    url(r'^admin/qes_body/add/(?P<query_id>\d+)/$', admin_qes_add),
    url(r'^admin/delete/(?P<query_id>\d+)/$', admin_qes_delete),
    url(r'^admin/delete/item/(?P<item_id>\d+)/$', admin_qes_delete_item),
    url(r'^admin/qes_body/edit/(?P<item_id>\d+)/$', admin_qes_edit),
    url(r'^admin/qes_body/action/(?P<query_id>\d+)/$', admin_qes_action),
    url(r'^admin/query/rename/(?P<query_id>\d+)/$', admin_query_rename),
    url(r'^admin/query/add/$', admin_query_add)

]