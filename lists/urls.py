from django.urls import path, re_path

from lists.views import view_list, new_list, add_item

urlpatterns = [
    re_path(r'^(\d+)/$', view_list, name='view_list'),
    re_path(r'^(\d+)/add$', add_item, name='add_item'),
    path('new', new_list, name='new_list'),
]
