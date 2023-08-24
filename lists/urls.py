from django.urls import path, re_path

from lists.views import home_page, view_list, new_list, add_item

urlpatterns = [
    path('', home_page, name='home'),
    re_path(r'^lists/(\d+)/$', view_list, name='view_list'),
    re_path(r'^lists/(\d+)/add$', add_item, name='add_item'),
    path('lists/new', new_list, name='new_list'),
]
