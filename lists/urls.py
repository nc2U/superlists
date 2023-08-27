from django.urls import path, re_path

from lists.views import view_list, add_list

urlpatterns = [
    path('add', add_list, name='add_list'),
    re_path(r'^(\d+)/$', view_list, name='view_list'),
]
