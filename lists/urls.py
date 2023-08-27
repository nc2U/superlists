from django.urls import path, re_path

from lists.views import view_list, new_list

urlpatterns = [
    re_path(r'^(\d+)/$', view_list, name='view_list'),
    path('new', new_list, name='new_list'),
]
